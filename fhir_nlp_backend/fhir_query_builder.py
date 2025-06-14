import spacy
from spacy.matcher import Matcher
from datetime import datetime, timedelta

class FHIRQueryBuilder:
    """
    A class to parse natural language queries and convert them into
    simulated FHIR API request URLs.
    """

    def __init__(self, fhir_base_url="https://fhir.example.com/r4"):
        """
        Initializes the FHIRQueryBuilder.

        Args:
            fhir_base_url (str): The base URL for the target FHIR server.
        """
        try:
            # Load the small English model for spaCy.
            # This model is efficient and sufficient for this task.
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")
            
        # The base URL for constructing FHIR API requests.
        self.fhir_base_url = fhir_base_url
        
        # Initialize the spaCy Matcher with the shared vocabulary.
        self.matcher = Matcher(self.nlp.vocab)
        self._setup_matchers()

        # A mapping of common condition names to their SNOMED CT codes.
        # This simulates a clinical terminology service.
        self.condition_codes = {
            "diabetic": "44054006",
            "diabetes": "44054006",
            "hypertension": "38341003",
            "asthma": "195967001",
            "cancer": "363346000"
        }

    def _setup_matchers(self):
        """
        Defines and adds the pattern matching rules to the spaCy Matcher.
        This is where we define how to find entities like age, gender, and conditions.
        """
        # Pattern to find age conditions like "over 50", "under 30", "older than 45"
        age_pattern = [
            {"LOWER": {"IN": ["over", "older", "greater", "above", ">", "at least"]}},
            {"LOWER": {"IN": ["than"]}, "OP": "?"},
            {"IS_DIGIT": True}
        ]
        
        age_pattern_under = [
            {"LOWER": {"IN": ["under", "younger", "less", "below", "<"]}},
            {"LOWER": {"IN": ["than"]}, "OP": "?"},
            {"IS_DIGIT": True}
        ]

        # Pattern to find age with 'years old' format
        age_years_pattern = [
            {"IS_DIGIT": True},
            {"LOWER": {"IN": ["years", "year"]}},
            {"LOWER": {"IN": ["old", "of", "age"]}, "OP": "?"}
        ]

        # Pattern to find gender
        gender_pattern = [
            {"LOWER": {"IN": ["male", "female", "man", "woman", "men", "women"]}}
        ]

        # Add the defined patterns to the matcher with unique names.
        self.matcher.add("AGE_OVER", [age_pattern])
        self.matcher.add("AGE_UNDER", [age_pattern_under])
        self.matcher.add("AGE_YEARS", [age_years_pattern])
        self.matcher.add("GENDER", [gender_pattern])

    def _extract_entities(self, text: str) -> dict:
        """
        Processes the input text to extract key clinical and demographic entities.

        Args:
            text (str): The natural language query.

        Returns:
            dict: A dictionary containing the extracted entities.
        """
        doc = self.nlp(text)
        matches = self.matcher(doc)
        
        entities = {
            "conditions": [],
            "age_comparison": None,
            "age_value": None,
            "gender": None
        }

        # 1. Extract conditions by checking tokens against our dictionary.
        for token in doc:
            if token.lemma_.lower() in self.condition_codes:
                entities["conditions"].append(token.lemma_.lower())

        # 2. Extract age and gender from the matcher results.
        for match_id, start, end in matches:
            rule_id = self.nlp.vocab.strings[match_id]
            span = doc[start:end]
            
            if rule_id == "AGE_OVER":
                entities["age_comparison"] = "gt" # 'gt' for greater than
                try:
                    entities["age_value"] = int(span[-1].text)
                except ValueError:
                    # Handle case where we can't parse the age
                    continue
                
            elif rule_id == "AGE_UNDER":
                entities["age_comparison"] = "lt" # 'lt' for less than
                try:
                    entities["age_value"] = int(span[-1].text)
                except ValueError:
                    # Handle case where we can't parse the age
                    continue
            
            elif rule_id == "AGE_YEARS":
                # For now, assume this means "at least this age"
                entities["age_comparison"] = "gt"
                try:
                    entities["age_value"] = int(span[0].text)
                except ValueError:
                    # Handle case where we can't parse the age
                    continue

            elif rule_id == "GENDER":
                gender_token = span[0].text.lower()
                if gender_token in ["male", "man", "men"]:
                    entities["gender"] = "male"
                elif gender_token in ["female", "woman", "women"]:
                    entities["gender"] = "female"
        
        return entities

    def build_fhir_request(self, text: str) -> str:
        """
        Constructs a simulated FHIR API request URL from a natural language query.

        Args:
            text (str): The user's query.

        Returns:
            str: A string representing the simulated FHIR API request URL.
        """
        entities = self._extract_entities(text)
        
        # The resource we are searching for is 'Patient'
        request_url = f"{self.fhir_base_url}/Patient"
        params = []

        # Add gender parameter if found
        if entities["gender"]:
            params.append(f"gender={entities['gender']}")
        
        # Add age parameter if found
        if entities["age_comparison"] and entities["age_value"] is not None:
            # FHIR queries on age use the 'birthdate' parameter. We must
            # calculate the date from the age.
            current_year = datetime.now().year
            birth_year = current_year - entities["age_value"]
            
            # For "over 50", birthdate must be *before* (less than or equal to) the year that's 50 years ago
            # For "under 30", birthdate must be *after* (greater than or equal to) the year that's 30 years ago
            if entities["age_comparison"] == "gt":
                params.append(f"birthdate=le{birth_year}-01-01") # le = less than or equal
            elif entities["age_comparison"] == "lt":
                params.append(f"birthdate=ge{birth_year}-01-01") # ge = greater than or equal

        # Add condition parameters if found
        # This uses a chained parameter to search for Patients who have a specific Condition.
        for condition in entities["conditions"]:
            snomed_code = self.condition_codes.get(condition)
            if snomed_code:
                # The '_has' parameter links Patient to Condition resources.
                # Format: _has:Condition:patient:code={code}
                params.append(f"_has:Condition:patient:code={snomed_code}")
        
        # Join all parameters to form the final URL.
        if params:
            request_url += "?" + "&".join(params)
            
        return request_url

    def filter_patients_by_fhir_url(self, fhir_url: str, patients: list) -> list:
        """
        Filters a list of patients based on a FHIR request URL.

        Args:
            fhir_url (str): The FHIR request URL containing query parameters.
            patients (list): A list of patient dictionaries to filter.

        Returns:
            list: Filtered list of patients matching the FHIR query parameters.
        """
        # If there are no query parameters, return all patients
        if '?' not in fhir_url:
            return patients
        
        # Extract query parameters from the URL
        query_part = fhir_url.split('?')[1]
        params = query_part.split('&')
        param_dict = {}
        
        # Parse parameters into a dictionary
        for param in params:
            if '=' in param:
                key, value = param.split('=', 1)
                param_dict[key] = value
        
        filtered_patients = patients
        
        # Filter by gender
        if 'gender' in param_dict:
            gender = param_dict['gender']
            filtered_patients = [p for p in filtered_patients if p['gender'] == gender]
        
        # Filter by birthdate (age)
        if 'birthdate' in param_dict:
            birthdate_param = param_dict['birthdate']
            
            # Handle birthdate less than or equal (patients older than X)
            if birthdate_param.startswith('le'):
                year_cutoff = int(birthdate_param[2:6])  # Extract year from 'le2022-01-01'
                filtered_patients = [
                    p for p in filtered_patients 
                    if int(p['birthDate'].split('-')[0]) <= year_cutoff
                ]
            
            # Handle birthdate greater than or equal (patients younger than X)
            elif birthdate_param.startswith('ge'):
                year_cutoff = int(birthdate_param[2:6])  # Extract year from 'ge2022-01-01'
                filtered_patients = [
                    p for p in filtered_patients 
                    if int(p['birthDate'].split('-')[0]) >= year_cutoff
                ]
        
        # Filter by conditions
        for key, value in param_dict.items():
            if key.startswith('_has:Condition:patient:code'):
                condition_code = value
                filtered_patients = [
                    p for p in filtered_patients 
                    if any(condition_code in condition for condition in p['conditions'])
                ]
        
        return filtered_patients


# --- Main execution block for testing ---
if __name__ == "__main__":
    builder = FHIRQueryBuilder()

    # --- Example Queries for Testing ---
    queries_to_test = [
        "Show me all diabetic patients over 50",
        "Find female patients with hypertension",
        "List all patients under 40 with asthma",
        "Show me all male patients",
        "Find patients with cancer and diabetes who are older than 65"
    ]

    print("--- FHIR Query Builder Test ---")
    for i, query in enumerate(queries_to_test):
        fhir_request_url = builder.build_fhir_request(query)
        print(f"\nQuery {i+1}: \"{query}\"")
        print(f"  -> FHIR Request: {fhir_request_url}")