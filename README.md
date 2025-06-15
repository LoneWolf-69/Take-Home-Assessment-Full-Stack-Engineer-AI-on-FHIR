# FHIR AI Query System - Full Stack Healthcare Application

> **AI-powered healthcare data querying tool that converts natural language into FHIR-compliant API requests**

[![Live Demo]](https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app)
[![Backend API]](https://fhir-query-backend.onrender.com)

## 🎯 Overview

This project demonstrates production-ready healthcare application development by creating an intelligent FHIR data querying system. Healthcare professionals can query patient data using natural language, automatically converted into structured FHIR API calls.

**🌟 Live Demo**: [https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app](https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app)

## 🚀 Key Features

✅ **Full-Stack Development**: Complete end-to-end application  
✅ **AI/NLP Integration**: spaCy + OpenAI for medical query processing  
✅ **FHIR Compliance**: Healthcare standards-compliant data handling  
✅ **Production Deployment**: Cloud-hosted on Vercel + Render  
✅ **Modern Tech Stack**: Next.js 14, Python 3.13, TypeScript  

## 🏗️ Architecture

```
Frontend (Next.js) ◄──── API Calls ────► Backend (Python/Flask)
• Search UI                              • NLP Processing
• Data Visualization                     • FHIR Mapping
• Interactive Filters                    • OpenAI Integration
• Charts & Tables                        • Patient Simulation
```

## 🛠️ Part 1: Backend & NLP (Python)

**Technologies**: Python 3.13, Flask, spaCy, OpenAI API, Pydantic

### Quick Start:
```bash
cd fhir_nlp_backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
export OPENAI_API_KEY="your-key"  # Optional
python app.py
```

### Example Query Processing:
```json
Input: "Show me all diabetic patients over 50"
Output: {
  "fhir_request": "https://fhir.example.com/r4/Patient?birthdate=le1974-01-01&_has:Condition:patient:code=44054006",
  "parameters": {
    "age_filter": ">50",
    "condition": "diabetes",
    "snomed_code": "44054006"
  }
}
```

### API Endpoints:
- `POST /query` - Convert natural language to FHIR
- `POST /patients` - Get patient data from FHIR request
- `GET /suggestions` - Query suggestions
- `GET /health` - Health check

## 🎨 Part 2: Frontend UI (React/Next.js)

**Technologies**: Next.js 14, TypeScript, Chart.js, Tailwind CSS, Axios

### Features:
🔍 **Smart Search**: Real-time suggestions, input validation  
📊 **Data Visualization**: Gender/condition distribution charts  
📋 **Patient Management**: Sortable tables with pagination  
🌐 **UX**: Responsive design, multilingual support (EN/ES), offline fallback 

### Quick Start:
```bash
cd fhir-query-ui
npm install
echo "NEXT_PUBLIC_API_URL=https://fhir-query-backend.onrender.com" > .env.local
npm run dev
```

### Part 3: Security & Compliance (HIPAA)

**Task Overview:**
Write a technical document on ensuring HIPAA compliance and secure FHIR data handling.

**📋 Deliverable**: [Security & Compliance.pdf]

## 🚀 Deployment

### Production URLs:
- **Frontend**: [https://fhir-ai-query-bufdn81cl-lonewolf-69s-projects.vercel.app]
- **Backend API**: [https://fhir-query-backend.onrender.com]

### Deployment Commands:

```bash
# Backend (Render)
git push origin main  # Auto-deploys via GitHub integration

# Frontend (Vercel)
npm run build
vercel --prod
```

## 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.13 + Flask | API service and NLP processing |
| **NLP** | spaCy + OpenAI API | Medical entity extraction |
| **Frontend** | Next.js 14 + TypeScript | Modern React application |
| **Styling** | Tailwind CSS | Responsive design |
| **Charts** | Chart.js | Data visualization |
| **API Client** | Axios | HTTP requests |
| **Deployment** | Vercel + Render | Cloud hosting |
| **Version Control** | GitHub | Source code management |

## 📝 Notes & Future Improvements

### 🎯 Focus of This Implementation

My primary focus for this assessment was on creating a robust, end-to-end user experience that seamlessly integrates a sophisticated NLP backend with a polished, modern frontend. Emphasis was placed on clean architecture, comprehensive functionality, and adherence to the core requirements of all three parts of the assessment.

### 🚀 Potential Improvements with More Time

Given additional time, I would pursue the following enhancements to further elevate the project to a production-grade enterprise application:

🐳 **Containerization**: Implement Docker and Docker Compose to containerize both the frontend and backend services. This would streamline the development setup, guarantee environment consistency, and simplify production deployment.

🧠 **Advanced NLP & Intent Handling**: While spaCy's rule-based matching is effective, I would integrate a transformer-based model (like BioBERT) or a Large Language Model (LLM) to handle more complex and ambiguous queries, such as those involving date ranges, symptom descriptions, or medication history.

⚡ **Comprehensive State Management**: For the frontend, I would introduce a dedicated state management library like Zustand or Redux Toolkit to more formally manage API state, caching, and complex UI interactions, especially as the application scales.

🌍 **Enhanced Internationalization (i18n)**: Fully implement multi-language support on the frontend using a library like react-i18next, providing translated interfaces for global accessibility beyond the current English/Spanish support.

🔄 **CI/CD Pipeline**: Establish a continuous integration and deployment pipeline using GitHub Actions to automate testing, linting, and deployments to Vercel and a production backend service.

🔒 **Real FHIR Integration**: Connect to actual FHIR servers (like HAPI FHIR) instead of simulated data, implementing proper authentication and real patient data handling.

📊 **Advanced Analytics**: Add more sophisticated data visualization options, export capabilities, and dashboard features for healthcare administrators.


This project was built as a take-home assessment demonstrating full-stack development capabilities in the healthcare AI domain. The implementation showcases:

- **Modern Development Practices**: TypeScript, RESTful APIs, responsive design
- **Healthcare Standards**: FHIR compliance, HIPAA security considerations  
- **AI Integration**: Natural language processing with medical terminology
- **Production Readiness**: Deployed services, error handling, fallback systems

*This application demonstrates the potential of AI-powered tools to make healthcare data more accessible and actionable for medical professionals.*