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

**What I Built:**
- Python Flask API service with advanced NLP capabilities
- Intelligent query parser using spaCy and OpenAI GPT models
- FHIR-compliant data structure simulation
- RESTful API with comprehensive error handling

**Technologies Used:**
- **Python 3.13** with Flask framework
- **spaCy NLP** with medical entity recognition
- **OpenAI API** for enhanced query understanding
- **Pydantic** for data validation
- **CORS** for cross-origin requests

**Key Features:**
```python
# Example: Natural language to FHIR conversion
Input: "Show me all diabetic patients over 50"
Output: {
  "resourceType": "Bundle",
  "entry": [
    {
      "resource": {
        "resourceType": "Patient",
        "age": 52,
        "condition": "Diabetes Mellitus Type 2"
      }
    }
  ]
}

**Supported Query Types:**
1. Age-based filtering: *"patients over 65"*
2. Condition-based search: *"diabetic patients"*
3. Gender-specific queries: *"female patients with hypertension"*
4. Complex multi-criteria: *"male patients over 40 with diabetes or heart disease"*
5. Age range queries: *"patients between 30 and 65 with asthma"*

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