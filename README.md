# 🔍 AI Log Analyzer

> A full-stack web application that automatically detects anomalies, analyzes root causes, and suggests solutions from uploaded log files using AI.

![Next.js](https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=next.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.129-009688?style=flat-square&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-ready-326CE5?style=flat-square&logo=kubernetes)

---

## 🚀 Project Overview

**AI Log Analyzer** is a portfolio project built to practice DevOps and cloud-native development workflows.

Upload a server log file (.log / .txt) and get:
- 📋 Log file parsing with instant preview
- 🤖 AI-powered automatic error pattern detection
- 🔎 Root cause estimation and actionable solutions

---

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| Frontend | Next.js 15 (TypeScript), Tailwind CSS |
| Backend | FastAPI (Python) |
| AI | Google Gemini API / OpenAI API |
| Containerization | Docker |
| Orchestration | Kubernetes |
| IaC | Terraform |
| CI/CD | GitHub Actions |

---

## 📂 Project Structure

```
ai-log-analyzer/
├── backend/                # FastAPI application
│   ├── routes/
│   │   └── analyze.py      # File upload & analysis API
│   ├── services/
│   │   └── ai_service.py   # AI integration logic
│   ├── uploads/            # Stored log files
│   └── main.py             # Entry point
├── frontend/               # Next.js application
│   └── src/
│       └── app/
│           └── page.tsx    # Main UI
├── k8s/                    # Kubernetes manifests
├── terraform/              # Infrastructure as Code
├── .github/workflows/      # GitHub Actions CI/CD
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- AI API Key (Gemini or OpenAI)

### Run Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

uvicorn main:app --reload
```

Swagger UI available at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Run Frontend

```bash
cd frontend
npm install
npm run dev -- -p 3001
```

Frontend available at: [http://localhost:3001](http://localhost:3001)

---

## 🎯 Key Features

### 📁 Log File Upload
- Supports `.log` and `.txt` file formats
- Uploaded files are stored and managed on the server

### 🤖 AI-Powered Analysis
- Automatic detection of ERROR and CRITICAL log patterns
- Natural language root cause estimation and fix suggestions

### 📊 Result Dashboard
- File metadata display (filename, line count)
- Log content preview
- Real-time AI analysis results

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/api/analyze` | Upload log file & run AI analysis |

---

## 🗺 Roadmap

- [x] FastAPI backend setup
- [x] Next.js frontend setup
- [x] Frontend ↔ Backend integration
- [x] Log file upload
- [x] AI analysis integration
- [ ] Docker containerization
- [ ] Kubernetes deployment
- [ ] GitHub Actions CI/CD pipeline
- [ ] Terraform IaC

---

## 👨‍💻 Author

Made with ❤️ as a DevOps portfolio project
