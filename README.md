# FHIR AI Query System - Full Stack Healthcare Application

> **A sophisticated AI-powered healthcare data querying tool that converts natural language into FHIR-compliant API requests**

## 🎯 Project Overview

This project demonstrates my ability to build production-ready healthcare applications by creating an intelligent FHIR (Fast Healthcare Interoperability Resources) data querying system. The application allows healthcare professionals to query patient data using natural language, automatically converting their requests into structured FHIR API calls.

**Live Demo**: [https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app]

## 🚀 Key Achievements

✅ **Full-Stack Development**: Built complete end-to-end application  
✅ **AI/NLP Integration**: Implemented sophisticated natural language processing  
✅ **Healthcare Standards**: FHIR-compliant data handling and API design  
✅ **Production Deployment**: Successfully deployed on cloud platforms  
✅ **Modern Tech Stack**: Used industry-standard technologies and best practices  

## 🛠️ Technical Implementation

# FHIR AI Query System - Full Stack Healthcare Application

> **A sophisticated AI-powered healthcare data querying tool that converts natural language into FHIR-compliant API requests**

## 🎯 Project Overview

This project demonstrates my ability to build production-ready healthcare applications by creating an intelligent FHIR (Fast Healthcare Interoperability Resources) data querying system. The application allows healthcare professionals to query patient data using natural language, automatically converting their requests into structured FHIR API calls.

**Live Demo**: [https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app]

## 🚀 Key Achievements

✅ **Full-Stack Development**: Built complete end-to-end application  
✅ **AI/NLP Integration**: Implemented sophisticated natural language processing  
✅ **Healthcare Standards**: FHIR-compliant data handling and API design  
✅ **Production Deployment**: Successfully deployed on cloud platforms  
✅ **Modern Tech Stack**: Used industry-standard technologies and best practices  

## 🛠️ Technical Implementation

### Part 1: Backend & NLP Integration (Python)

**Task Overview:**
Build a Python-based service that accepts natural language input (e.g., "Show me all diabetic patients over 50") and converts it into a simulated FHIR API request.

**Requirements Implemented:**
- ✅ **NLP Library Integration**: Used spaCy for entity extraction and intent recognition
- ✅ **FHIR API Simulation**: Created Patient and Condition resource mappings
- ✅ **Example Mappings**: Provided comprehensive input/output examples

How To Run:
# Clone repository
git clone <[repository-url](https://github.com/LoneWolf-69/Take-Home-Assessment-Full-Stack-Engineer-AI-on-FHIR.git)>
cd fhir_nlp_backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
# If you are using the Fish Shell
source venv/bin/activate.fish

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run the application
python fhir_query_builder.py
# To connect with the frontend and run the queries on next.js screen
python app.py

**What I Built:**
- Python Flask API service with advanced NLP capabilities
- Intelligent query parser using spaCy and OpenAI GPT models
- FHIR-compliant data structure simulation
- RESTful API with comprehensive error handling

**Technologies Used:**
- **Python 3.13** with Flask framework
- **spaCy NLP** with medical entity recognition (`en_core_web_sm` model)
- **OpenAI API** for enhanced query understanding
- **Pydantic** for data validation
- **CORS** for cross-origin requests

**NLP Entity Extraction Process:**
```python
# Natural Language Processing Pipeline
1. Text preprocessing and tokenization
2. Medical entity recognition (conditions, age, gender)
3. Intent classification (search, filter, find)
4. Parameter extraction (age ranges, medical codes)
5. FHIR query construction

Example 1: Age and Condition Query
Input: "Show me all diabetic patients over 50"

NLP Extraction:
- Intent: "search"
- Condition: "diabetes" → SNOMED: 44054006
- Age Filter: ">50" → birthdate: "le1974-01-01"
- Resource: "Patient"

FHIR Output:
{
  "query": "Show me all diabetic patients over 50",
  "fhir_request": "https://fhir.example.com/r4/Patient?birthdate=le1974-01-01&_has:Condition:patient:code=44054006",
  "parameters": {
    "age_filter": ">50",
    "condition": "diabetes",
    "snomed_code": "44054006"
  }
}

Example 2: Gender-Specific Query
Input: "Find female patients with hypertension"

NLP Extraction:
- Intent: "find"
- Gender: "female"
- Condition: "hypertension" → SNOMED: 38341003
- Resource: "Patient"

FHIR Output:
{
  "query": "Find female patients with hypertension",
  "fhir_request": "https://fhir.example.com/r4/Patient?gender=female&_has:Condition:patient:code=38341003",
  "parameters": {
    "gender": "female",
    "condition": "hypertension",
    "snomed_code": "38341003"
  }
}


### Part 2: Frontend UI (React/Next.js)

**What I Built:**
- Modern, responsive React application using Next.js 14
- Intelligent search interface with auto-complete
- Interactive data visualizations and comprehensive filtering
- Multilingual support (English/Spanish)

**Technologies Used:**
- **Next.js 14** with TypeScript
- **Material-UI (MUI)** for professional UI components
- **Chart.js** for interactive data visualization
- **Tailwind CSS** for responsive design
- **Axios** for API integration

**Key Features:**

🔍 **Smart Search Interface**
- Real-time query suggestions
- Input validation and error handling
- Search history tracking

📊 **Data Visualization**
- Gender distribution bar charts
- Condition prevalence analytics
- Interactive filtering system

📋 **Patient Management**
- Comprehensive patient data table
- Sortable columns with pagination
- Age range and condition filters

🌐 **User Experience**
- Responsive design for all devices
- Loading states and error handling
- Multilingual interface support