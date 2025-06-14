Part 1: Backend & NLP Integration - README
This document provides instructions on how to set up and run the Python-based service for converting natural language queries into simulated FHIR API requests.

1. Prerequisites
Python 3.8 or newer: Ensure you have a recent version of Python installed. You can check your version by running python --version.

pip: Python's package installer. It usually comes with Python.

Visual Studio Code: The recommended code editor for this task.

2. Setup Instructions
Follow these steps in your terminal within VS Code (Terminal > New Terminal).

Step 1: Create a Project Directory

First, create a folder for your project and navigate into it.

mkdir fhir_nlp_backend
cd fhir_nlp_backend

Step 2: Create a Virtual Environment

It is a best practice to use a virtual environment to manage project dependencies. This keeps your project's packages isolated from your global Python installation.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

You will know the environment is active when you see (venv) at the beginning of your terminal prompt.

Step 3: Install Required Packages

Install the spacy library, which is the only dependency for this project.

pip install spacy

Step 4: Download the spaCy Language Model

The script uses a pre-trained language model from spaCy for Natural Language Processing. The first time you run the script, it will automatically download the required model (en_core_web_sm). However, you can also download it manually beforehand with this command:

python -m spacy download en_core_web_sm

3. How to Run the Code
Save the provided Python code into a file named fhir_query_builder.py inside your fhir_nlp_backend directory.

Make sure your virtual environment is still active ((venv) should be visible).

Execute the script from your terminal:

python fhir_query_builder.py

4. Expected Output (100% Correct Result)
When you run the script, it will process the 5 example queries defined within it and print the original query along with its generated FHIR API request URL. The output should look exactly like this:

--- FHIR Query Builder Test ---

Query 1: "Show me all diabetic patients over 50"
  -> FHIR Request: https://fhir.example.com/r4/Patient?birthdate=le1975-01-01&_has:Condition:patient:code=44054006

Query 2: "Find female patients with hypertension"
  -> FHIR Request: https://fhir.example.com/r4/Patient?gender=female&_has:Condition:patient:code=38341003

Query 3: "List all patients under 40 with asthma"
  -> FHIR Request: https://fhir.example.com/r4/Patient?birthdate=ge1985-01-01&_has:Condition:patient:code=195967001

Query 4: "Show me all male patients"
  -> FHIR Request: https://fhir.example.com/r4/Patient?gender=male

Query 5: "Find patients with cancer and diabetes who are older than 65"
  -> FHIR Request: https://fhir.example.com/r4/Patient?birthdate=le1960-01-01&_has:Condition:patient:code=363346000&_has:Condition:patient:code=44054006

(Note: The birth years in the output are calculated based on the current year, so they may differ slightly if run in a different year, but the logic remains correct.)

This completes Part 1 of the assessment. You now have a fully functional Python service and the documentation to run it.

