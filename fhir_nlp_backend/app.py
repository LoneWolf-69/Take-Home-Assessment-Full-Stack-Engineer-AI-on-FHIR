from flask import Flask, request, jsonify
from flask_cors import CORS
from fhir_query_builder import FHIRQueryBuilder

# Initialize the Flask app
app = Flask(__name__)

# Configure CORS to accept all origins (for development purposes)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize the FHIR Query Builder
query_builder = FHIRQueryBuilder()

# Sample FHIR patient data for simulation
MOCK_PATIENTS = [
    {
        "id": '1', 
        "name": 'John Smith', 
        "gender": 'male', 
        "birthDate": '1960-04-12',
        "conditions": ['Diabetes Mellitus (44054006)']
    },
    {
        "id": '2', 
        "name": 'Mary Johnson', 
        "gender": 'female', 
        "birthDate": '1972-10-24',
        "conditions": ['Hypertension (38341003)']
    },
    {
        "id": '3', 
        "name": 'Robert Davis', 
        "gender": 'male', 
        "birthDate": '1951-02-14',
        "conditions": ['Diabetes Mellitus (44054006)', 'Hypertension (38341003)']
    },
    {
        "id": '4', 
        "name": 'Sarah Wilson', 
        "gender": 'female', 
        "birthDate": '1984-07-30',
        "conditions": ['Asthma (195967001)']
    },
    {
        "id": '5', 
        "name": 'Michael Brown', 
        "gender": 'male', 
        "birthDate": '1946-11-08',
        "conditions": ['Cancer (363346000)', 'Diabetes Mellitus (44054006)']
    },
    {
        "id": '6', 
        "name": 'Elizabeth Taylor', 
        "gender": 'female',
        "birthDate": '1992-05-17',
        "conditions": []
    },
    {
        "id": '7', 
        "name": 'James Lee', 
        "gender": 'male', 
        "birthDate": '1988-09-22',
        "conditions": ['Asthma (195967001)']
    },
    {
        "id": '8', 
        "name": 'Patricia Moore', 
        "gender": 'female', 
        "birthDate": '1976-03-05',
        "conditions": ['Hypertension (38341003)']
    }
]

# Add a test endpoint
@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    response = jsonify({'status': 'API is running'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Query endpoint to process natural language queries
@app.route('/query', methods=['POST', 'OPTIONS'])
def process_query():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
        
    # Handle the actual POST request
    data = request.json
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
        
    query_text = data.get('query', '')
    
    if not query_text:
        return jsonify({'error': 'No query provided'}), 400
    
    # Process the query using your FHIRQueryBuilder
    fhir_request = query_builder.build_fhir_request(query_text)
    
    # Return the simulated FHIR request URL
    return jsonify({
        'fhir_request': fhir_request
    })

# Add the patients endpoint to handle patient data retrieval based on FHIR request
@app.route('/patients', methods=['POST', 'OPTIONS'])
def get_patients():
    """
    Returns patient data matching a FHIR request URL
    """
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
        
    # Handle the actual POST request
    data = request.json
    fhir_request = data.get('fhir_request', '')
    
    if not fhir_request:
        return jsonify({'error': 'No FHIR request provided'}), 400
    
    # Filter patients based on the FHIR request parameters
    filtered_patients = query_builder.filter_patients_by_fhir_url(fhir_request, MOCK_PATIENTS)
    
    return jsonify({
        'patients': filtered_patients
    })

# Add suggestions endpoints for auto-complete feature
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    """
    Returns a list of suggested queries for the autocomplete feature.
    """
    # These are predefined suggestions that could help users get started
    suggestions = [
        "Show me all diabetic patients over 50",
        "Find female patients with hypertension",
        "List all patients under 40 with asthma",
        "Show me all male patients",
        "Find patients with cancer and diabetes who are older than 65",
        "Show me all female patients under 50",
        "Find patients with asthma",
        "List all patients over 60"
    ]
    
    return jsonify({'suggestions': suggestions})

@app.route('/suggestions/filter', methods=['POST'])
def filter_suggestions():
    """
    Returns filtered suggestions based on the partial query entered by the user.
    """
    data = request.json
    partial_query = data.get('partial_query', '').lower()
    
    if not partial_query or len(partial_query) < 2:
        return jsonify({'suggestions': []})
    
    base_suggestions = [
        "Show me all diabetic patients over 50",
        "Find female patients with hypertension",
        "List all patients under 40 with asthma",
        "Show me all male patients",
        "Find patients with cancer and diabetes who are older than 65",
        "Show me all female patients under 50",
        "Find patients with asthma",
        "List all patients over 60"
    ]
    
    # Filter suggestions based on partial_query
    filtered_suggestions = [s for s in base_suggestions if partial_query in s.lower()]
    
    return jsonify({'suggestions': filtered_suggestions})

# Run the Flask app
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))  # Use Render's PORT or default to 8000
    print(f"Flask server running on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port)  # Set debug=False for production