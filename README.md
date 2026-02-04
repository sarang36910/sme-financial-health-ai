🏦 SME Financial Health AI Platform
📌 Overview

The SME Financial Health AI Platform is an AI-powered web application designed to help Small and Medium Enterprises (SMEs) assess their financial health using uploaded financial data.
The platform analyzes revenue, expenses, and cash flow patterns to generate actionable insights, risk evaluation, industry benchmarking, and investor-ready summaries.

This solution is built to support non-finance business owners by presenting complex financial analysis in a simple, understandable format.

🎯 Problem Statement Addressed

SMEs often lack access to advanced financial analysis tools due to cost and complexity.
This platform solves that by providing:

Automated financial health assessment

Risk identification and scoring

Industry-specific benchmarking

Investor-ready financial summaries

Scalable backend with secure data storage

🚀 Key Features
✅ Financial Analysis

Total revenue, expenses, and profit calculation

Financial health score (0–100)

Risk categorization (Low / Moderate / High)

✅ Industry Benchmarking

Supports multiple industries (Retail, Manufacturing, Services, etc.)

Compares business performance against industry averages

✅ Actionable Insights

Identifies cost optimization needs

Generates investor-friendly insights

✅ File Upload Support

CSV / XLSX financial files

Automated parsing using pandas

✅ Database Integration

Stores financial reports securely in PostgreSQL

Enables report history tracking

✅ AI-Ready Architecture

Designed to support LLM-based insights (OpenAI / Claude)

Environment-based API key support

✅ Live Deployment

Fully deployed backend (publicly accessible)

🛠️ Tech Stack
Layer	Technology
Backend	FastAPI (Python)
Data Processing	pandas
Database	PostgreSQL
Deployment	Render
Frontend	React (basic dashboard)
Security	Environment variables, HTTPS
📂 Project Structure
sme-financial-health-ai/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── runtime.txt
│   └── database/
├── frontend/
│   └── react-dashboard/
├── README.md

🌐 Live Deployment

🔗 Backend API (Live):
https://sme-financial-health-ai.onrender.com

🔗 API Documentation (Swagger):
https://sme-financial-health-ai.onrender.com/docs

📊 Sample Output
{
  "business_summary": {
    "total_revenue": 37200,
    "total_expense": 24300,
    "profit": 12900,
    "financial_health_score": 74
  },
  "risk_overview": {
    "risk_level": "Moderate Risk"
  },
  "industry_comparison": {
    "industry": "Retail"
  },
  "investor_note": "Business is stable but requires cost optimization before scaling."
}

▶️ Demo Video

🎥 Demo Video (Public):
(Add your YouTube or Google Drive link here)

⚙️ How It Works (High Level)

User uploads a financial file (CSV/XLSX)

Backend parses and validates data

Financial metrics are calculated

Health score and risk level are generated

Industry benchmarking is applied

Results are stored in the database

Investor-ready insights are returned

🔐 Security & Compliance

All secrets handled using environment variables

HTTPS enforced via Render

No sensitive credentials committed to source code

📈 Future Enhancements

GST return integration

Banking API integration (loan & cash flow analysis)

Advanced AI recommendations

Multilingual support (Hindi & regional languages)

Visual dashboards with charts

👨‍💻 Author

Sarang P
Data Analyst | Aspiring Data Scientist
GitHub: https://github.com/sarang36910
