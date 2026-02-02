🧾 SME Financial Health Assessment Platform (AI-Powered)
📌 Overview

This project is an AI-powered financial health assessment platform designed for Small and Medium Enterprises (SMEs).
It analyzes uploaded financial data to generate actionable insights, risk assessment, and investor-ready reports through a full-stack application.

The system focuses on clarity, automation, and accessibility for non-finance business owners.

🚀 Key Features
🔹 Financial Analysis

Revenue, expense, and profit calculation

Profit margin and expense efficiency

Financial health scoring (0–100)

Risk classification (Low / Moderate / High)

🔹 AI-Ready Insights

Business performance summary

Cost optimization suggestions

Investor-focused insights

Designed for LLM-based recommendations

🔹 Forecasting & Risk Signals

Monthly expense aggregation

Burn-rate based risk indicators

Scalable for advanced forecasting models

🔹 Industry Awareness

Industry input (Retail, Manufacturing, Services, etc.)

Industry-specific context in reports

🔹 Multilingual Ready

Backend supports multilingual insight generation

Easily extendable to Hindi / regional languages

🔹 Full-Stack Architecture

Backend: FastAPI + Python (pandas)

Frontend: React.js

APIs: REST-based integration

File Upload: CSV / XLSX

🧠 System Architecture
React Frontend (Port 5173)
        ↓
FastAPI Backend (Port 8000)
        ↓
Pandas Data Processing
        ↓
JSON Financial Report

📂 Supported Input Formats

CSV (.csv)

Excel (.xlsx)

Required Columns:

Revenue

Expense

📊 Sample Output
{
  "business_summary": {
    "total_revenue": 37200,
    "total_expense": 24300,
    "profit": 12900,
    "financial_health_score": 74
  },
  "industry_comparison": {
    "industry": "Retail"
  },
  "risk_overview": {
    "risk_level": "Moderate Risk"
  },
  "investor_note": "Business is stable but requires cost optimization before scaling."
}

🛠️ Tech Stack
Layer	Technology
Frontend	React.js (Vite)
Backend	FastAPI
Data Processing	Python (pandas)
API	REST
File Handling	CSV / XLSX
Security	CORS enabled, no raw data persistence
▶️ How to Run the Project
🔹 Backend Setup
cd backend
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs

🔹 Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173

🧪 How to Use

Open the frontend URL

Upload a CSV or Excel file

Select the business industry

Click Analyze

View financial insights instantly

🔐 Security & Data Handling

No raw financial files are stored

Only derived insights are returned

Designed for secure API integration

Ready for encryption & compliance extensions

📈 Future Enhancements

GST return integration

Banking & NBFC API connections

Automated bookkeeping rules

Creditworthiness scoring

Advanced AI forecasting

Interactive data visualizations

🏆 Conclusion

This platform delivers a working MVP that demonstrates:

Real financial intelligence

Practical SME use-cases

Clean full-stack integration

Scalable AI-ready architecture

It is designed to be production-extendable, investor-friendly, and evaluation-ready.

👤 Author

Sarang P
MCA Graduate | Data Analyst | Aspiring Data Scientist