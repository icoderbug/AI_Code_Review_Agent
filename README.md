# 🤖 AI Code Review Agent

An AI-powered Code Review Platform built using **Python, Streamlit, Google Gemini API, and SQLite** that automatically analyzes source code for quality, risks, optimization opportunities, and best practices.

## 🚀 Live Demo

Add your deployed Render URL here:

```text
https://your-render-url.onrender.com
```

---

## 📌 Features

### 🔍 Automated Code Review

* Reviews Python source code using Google Gemini AI.
* Identifies code smells and potential issues.
* Provides actionable improvement suggestions.

### ⚡ Code Optimization Analysis

* Detects inefficient code patterns.
* Suggests performance improvements.
* Recommends cleaner implementations.

### 🛡️ Risk Assessment

* Finds potential security vulnerabilities.
* Highlights risky coding practices.
* Suggests safer alternatives.

### ⭐ Quality Analysis

* Evaluates readability and maintainability.
* Reviews coding standards compliance.
* Provides quality scores and recommendations.

### 📄 PDF Report Generation

* Generates downloadable review reports.
* Professional summary format.
* Easy sharing and documentation.

### 📊 Review History

* Stores previous code reviews.
* Allows users to revisit generated reports.

---

## 🏗️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API

### Database

* SQLite

### Reporting

* ReportLab PDF Generator

### Deployment

* Render

---

## 📂 Project Structure

```text
AI_CODE_REVIEW_AGENT/
│
├── agents/
│   ├── code_review_agent.py
│   ├── language_agent.py
│   ├── optimization_agent.py
│   ├── quality_agent.py
│   └── risk_agent.py
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── config.py
├── database.py
├── pdf_generator.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/icoderbug/AI_Code_Review_Agent.git
cd AI_Code_Review_Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Upload a Python source file.
2. Click Analyze.
3. Review:

   * Code Review
   * Quality Analysis
   * Risk Analysis
   * Optimization Suggestions
4. Download the generated PDF report.

---

## 🎯 Future Enhancements

* Multi-language code support
* GitHub repository analysis
* CI/CD integration
* Docker deployment
* Team collaboration dashboard
* PostgreSQL migration
* AI-powered code fixes

---

## 👨‍💻 Author

**Prateek Singh**

B.Tech Computer Science Engineering (AKTU)

GitHub: https://github.com/icoderbug

---

## 📜 License

This project is licensed under the MIT License.
