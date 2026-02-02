


# from fastapi import FastAPI, UploadFile, File, Query
# import pandas as pd
# from io import BytesIO
# import numpy as np
# from sklearn.linear_model import LinearRegression
# import os
# from openai import OpenAI
# import os
# from database import SessionLocal
# from models import FinancialReport
# from fastapi.middleware.cors import CORSMiddleware

# # 🔴 Disable broken proxy variables
# os.environ.pop("http_proxy", None)
# os.environ.pop("https_proxy", None)
# os.environ.pop("HTTP_PROXY", None)
# os.environ.pop("HTTPS_PROXY", None)




# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# app = FastAPI(title="SME Financial Health AI")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# INDUSTRY_BENCHMARKS = {
#     "Retail": {
#         "profit_margin": 0.18,
#         "expense_ratio": 0.82
#     },
#     "Manufacturing": {
#         "profit_margin": 0.22,
#         "expense_ratio": 0.78
#     },
#     "Services": {
#         "profit_margin": 0.30,
#         "expense_ratio": 0.70
#     }
# }


# app = FastAPI(title="SME Financial Health AI")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# INDUSTRY_BENCHMARKS = {
#     "Retail": {
#         "profit_margin": 0.18,
#         "expense_ratio": 0.82
#     },
#     "Manufacturing": {
#         "profit_margin": 0.22,
#         "expense_ratio": 0.78
#     },
#     "Services": {
#         "profit_margin": 0.30,
#         "expense_ratio": 0.70
#     }
# }


# @app.get("/")
# def root():
#     return {"status": "Backend is running"}

# @app.post("/financial-health/")
# async def financial_health(file: UploadFile = File(...)):
#     if not file.filename.endswith((".csv", ".xlsx")):
#         return {"error": "Only CSV or XLSX files are supported"}

#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     required_cols = {"Revenue", "Expense"}
#     if not required_cols.issubset(df.columns):
#         return {
#             "error": "File must contain Revenue and Expense columns",
#             "found_columns": list(df.columns)
#         }

#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense

#     # Ratios
#     profit_margin = (profit / total_revenue) if total_revenue > 0 else 0
#     expense_ratio = (total_expense / total_revenue) if total_revenue > 0 else 1

#     # Monthly burn rate (avg expense per month)
#     if "Date" in df.columns:
#         df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
#         months = df["Date"].dt.to_period("M").nunique()
#         burn_rate = total_expense / months if months > 0 else total_expense
#     else:
#         burn_rate = total_expense

#     # Simple Health Score (0–100)
#     score = 100
#     score -= expense_ratio * 40
#     if profit < 0:
#         score -= 30
#     if burn_rate > (total_revenue / 2):
#         score -= 20

#     score = max(0, min(100, round(score)))

#     # Plain English insight
#     if score >= 75:
#         insight = "Financially healthy. Business shows good cost control and profitability."
#     elif score >= 50:
#         insight = "Moderate financial health. Expenses need closer monitoring."
#     else:
#         insight = "Financial risk detected. Immediate cost control is recommended."

#     return {
#         "total_revenue": round(float(total_revenue), 2),
#         "total_expense": round(float(total_expense), 2),
#         "profit": round(float(profit), 2),
#         "profit_margin_percent": round(profit_margin * 100, 2),
#         "expense_ratio_percent": round(expense_ratio * 100, 2),
#         "monthly_burn_rate": round(float(burn_rate), 2),
#         "financial_health_score": score,
#         "insight": insight
#     }
# from fastapi import Query

# @app.post(
#     "/industry-benchmark/",
#     operation_id="industry_benchmark_analysis"
# )
# async def industry_benchmark(
#     industry: str = Query(..., description="Retail / Manufacturing / Services"),
#     file: UploadFile = File(...)
# ):
#     if industry not in INDUSTRY_BENCHMARKS:
#         return {
#             "error": "Invalid industry",
#             "supported_industries": list(INDUSTRY_BENCHMARKS.keys())
#         }

#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense

#     company_profit_margin = profit / total_revenue if total_revenue > 0 else 0
#     company_expense_ratio = total_expense / total_revenue if total_revenue > 0 else 1

#     benchmark = INDUSTRY_BENCHMARKS[industry]

#     return {
#         "industry": industry,
#         "company_profit_margin_percent": round(company_profit_margin * 100, 2),
#         "industry_avg_profit_margin_percent": benchmark["profit_margin"] * 100,
#         "profit_margin_status": "Above Industry Average"
#         if company_profit_margin >= benchmark["profit_margin"]
#         else "Below Industry Average",

#         "company_expense_ratio_percent": round(company_expense_ratio * 100, 2),
#         "industry_avg_expense_ratio_percent": benchmark["expense_ratio"] * 100,
#         "expense_efficiency_status": "Efficient"
#         if company_expense_ratio <= benchmark["expense_ratio"]
#         else "Needs Optimization"
#     }
# from fastapi import Query

# @app.post(
#     "/industry-benchmark/",
#     operation_id="industry_benchmark_analysis"
# )
# async def industry_benchmark(
#     industry: str = Query(..., description="Retail / Manufacturing / Services"),
#     file: UploadFile = File(...)
# ):
#     if industry not in INDUSTRY_BENCHMARKS:
#         return {
#             "error": "Invalid industry",
#             "supported_industries": list(INDUSTRY_BENCHMARKS.keys())
#         }

#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense

#     company_profit_margin = profit / total_revenue if total_revenue > 0 else 0
#     company_expense_ratio = total_expense / total_revenue if total_revenue > 0 else 1

#     benchmark = INDUSTRY_BENCHMARKS[industry]

#     return {
#         "industry": industry,

#         "company_profit_margin_percent": round(company_profit_margin * 100, 2),
#         "industry_avg_profit_margin_percent": benchmark["profit_margin"] * 100,
#         "profit_margin_status":
#             "Above Industry Average"
#             if company_profit_margin >= benchmark["profit_margin"]
#             else "Below Industry Average",

#         "company_expense_ratio_percent": round(company_expense_ratio * 100, 2),
#         "industry_avg_expense_ratio_percent": benchmark["expense_ratio"] * 100,
#         "expense_efficiency_status":
#             "Efficient"
#             if company_expense_ratio <= benchmark["expense_ratio"]
#             else "Needs Cost Optimization"
#     }

#     from sklearn.linear_model import LinearRegression
# import numpy as np

# @app.post("/financial-forecast/")
# async def financial_forecast(file: UploadFile = File(...)):
#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     if not {"Date", "Revenue", "Expense"}.issubset(df.columns):
#         return {"error": "File must contain Date, Revenue, Expense columns"}

#     df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
#     df = df.dropna(subset=["Date"])

#     df["MonthIndex"] = np.arange(len(df))

#     # Revenue forecast
#     X = df[["MonthIndex"]]
#     y_rev = df["Revenue"]
#     y_exp = df["Expense"]

#     rev_model = LinearRegression()
#     exp_model = LinearRegression()

#     rev_model.fit(X, y_rev)
#     exp_model.fit(X, y_exp)

#     future_months = np.array([[len(df) + i] for i in range(6)])

#     future_revenue = rev_model.predict(future_months)
#     future_expense = exp_model.predict(future_months)

#     forecast = []
#     for i in range(6):
#         forecast.append({
#             "month": f"Month {i+1}",
#             "forecast_revenue": round(float(future_revenue[i]), 2),
#             "forecast_expense": round(float(future_expense[i]), 2),
#             "forecast_profit": round(float(future_revenue[i] - future_expense[i]), 2)
#         })

#     risk = "High Risk" if any(f["forecast_profit"] < 0 for f in forecast) else "Low Risk"

#     return {
#         "forecast_horizon": "6 Months",
#         "risk_level": risk,
#         "forecast": forecast
#     }

# @app.post("/financial-report/")
# async def financial_report(
#     industry: str = Query(..., description="Retail / Manufacturing / Services"),
#     file: UploadFile = File(...)
# ):
#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     # --- Core calculations ---
#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense

#     profit_margin = (profit / total_revenue) * 100 if total_revenue > 0 else 0
#     expense_ratio = (total_expense / total_revenue) * 100 if total_revenue > 0 else 0

#     # --- Health Score ---
#     score = 100
#     score -= expense_ratio * 0.4
#     if profit < 0:
#         score -= 30
#     score = max(0, min(100, round(score)))

#     # --- Industry benchmark ---
#     benchmark = INDUSTRY_BENCHMARKS[industry]
#     margin_status = (
#         "Above Industry Average"
#         if profit_margin / 100 >= benchmark["profit_margin"]
#         else "Below Industry Average"
#     )

#     # --- Simple forecast insight ---
#     df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
#     monthly_expense = df.groupby(df["Date"].dt.to_period("M"))["Expense"].sum()
#     burn_rate = monthly_expense.mean()

#     # --- Final report ---
#     report = {
#         "business_summary": {
#             "total_revenue": round(float(total_revenue), 2),
#             "total_expense": round(float(total_expense), 2),
#             "profit": round(float(profit), 2),
#             "profit_margin_percent": round(profit_margin, 2),
#             "financial_health_score": score
#         },
#         "industry_comparison": {
#             "industry": industry,
#             "profit_margin_status": margin_status
#         },
#         "risk_overview": {
#             "monthly_burn_rate": round(float(burn_rate), 2),
#             "risk_level": "High Risk" if score < 50 else "Moderate Risk" if score < 75 else "Low Risk"
#         },
#         "investor_note": (
#             "Business shows strong fundamentals and controlled expenses."
#             if score >= 75
#             else "Business is stable but requires cost optimization before scaling."
#         )
#     }
#     # --- Save to Database ---
#     db = SessionLocal()
#     db_report = FinancialReport(
#         industry=industry,
#         total_revenue=float(total_revenue),
#         total_expense=float(total_expense),
#         profit=float(profit),
#         health_score=score,
#         insight=report["investor_note"]
#     )
#     db.add(db_report)
#     db.commit()
#     db.close()

#     return report

# @app.post("/financial-report-multilingual/")
# async def financial_report_multilingual(
#     language: str = Query("en", description="en / hi"),
#     industry: str = Query(...),
#     file: UploadFile = File(...)
# ):
#     contents = await file.read()

#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(BytesIO(contents))
#     else:
#         df = pd.read_excel(BytesIO(contents))

#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense
#     profit_margin = (profit / total_revenue) * 100 if total_revenue > 0 else 0

#     score = 100
#     score -= (total_expense / total_revenue) * 40 if total_revenue > 0 else 40
#     if profit < 0:
#         score -= 30
#     score = max(0, min(100, round(score)))

#     insight_en = (
#         "Business is financially healthy and performing well."
#         if score >= 75
#         else "Business performance is moderate and needs cost optimization."
#         if score >= 50
#         else "Business is financially weak and requires urgent attention."
#     )

#     if language == "en":
#         insight = insight_en
#     else:
#         prompt = f"""
#         Translate the following financial insight into simple Hindi language
#         suitable for small business owners:

#         "{insight_en}"
#         """

#         response = client.chat.completions.create(
#             model="gpt-5",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.2
#         )

#         insight = response.choices[0].message.content

#     return {
#         "language": language,
#         "financial_health_score": score,
#         "profit_margin_percent": round(profit_margin, 2),
#         "insight": insight
#     }
# @app.get("/financial-reports/")
# def get_financial_reports():
#     db = SessionLocal()
#     reports = db.query(FinancialReport).order_by(FinancialReport.created_at.desc()).all()
#     db.close()

#     return [
#         {
#             "id": r.id,
#             "industry": r.industry,
#             "total_revenue": r.total_revenue,
#             "total_expense": r.total_expense,
#             "profit": r.profit,
#             "health_score": r.health_score,
#             "insight": r.insight,
#             "created_at": r.created_at
#         }
#         for r in reports
#     ]





# from fastapi import FastAPI, UploadFile, File, Query
# from fastapi.middleware.cors import CORSMiddleware
# import pandas as pd

# app = FastAPI(title="SME Financial Health API")

# # -----------------------------
# # CORS (MANDATORY FOR REACT)
# # -----------------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -----------------------------
# # ROOT CHECK
# # -----------------------------
# @app.get("/")
# def root():
#     return {"status": "Backend is running"}

# # -----------------------------
# # MAIN ENDPOINT (USED BY FRONTEND)
# # -----------------------------
# @app.post("/financial-report/")
# async def financial_report(
#     file: UploadFile = File(...),
#     industry: str = Query(...)
# ):
#     # Read CSV or Excel safely
#     if file.filename.endswith(".csv"):
#         df = pd.read_csv(file.file)
#     elif file.filename.endswith(".xlsx"):
#         df = pd.read_excel(file.file)
#     else:
#         return {"error": "Unsupported file format"}

#     # ---- BASIC VALIDATION ----
#     if "Revenue" not in df.columns or "Expense" not in df.columns:
#         return {"error": "CSV must contain Revenue and Expense columns"}

#     total_revenue = df["Revenue"].sum()
#     total_expense = df["Expense"].sum()
#     profit = total_revenue - total_expense

#     profit_margin = (profit / total_revenue) * 100 if total_revenue > 0 else 0

#     # ---- SIMPLE HEALTH SCORE ----
#     score = 100
#     score -= (total_expense / total_revenue) * 40 if total_revenue > 0 else 40
#     score = max(0, min(100, round(score)))

#     risk_level = (
#         "High Risk" if score < 50
#         else "Moderate Risk" if score < 75
#         else "Low Risk"
#     )

#     # -----------------------------
#     # FINAL RESPONSE (FRONTEND EXPECTS THIS)
#     # -----------------------------
#     return {
#         "business_summary": {
#             "total_revenue": round(float(total_revenue), 2),
#             "total_expense": round(float(total_expense), 2),
#             "profit": round(float(profit), 2),
#             "financial_health_score": score
#         },
#         "industry_comparison": {
#             "industry": industry,
#             "profit_margin_percent": round(profit_margin, 2)
#         },
#         "risk_overview": {
#             "risk_level": risk_level
#         },
#         "investor_note": (
#             "Business is stable but requires cost optimization before scaling."
#             if score < 75
#             else "Business shows strong financial fundamentals."
#         )
#     }




from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/financial-report/")
async def financial_report(
    file: UploadFile = File(...),
    industry: str = Query(...)
):
    contents = await file.read()

    if file.filename.endswith(".csv"):
        df = pd.read_csv(BytesIO(contents))
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(BytesIO(contents))
    else:
        return {"error": "Unsupported file type"}

    # ---- calculations ----
    total_revenue = df["Revenue"].sum()
    total_expense = df["Expense"].sum()
    profit = total_revenue - total_expense

    score = max(0, min(100, round(100 - (total_expense / total_revenue) * 40)))

    risk_level = (
        "High Risk" if score < 50
        else "Moderate Risk" if score < 75
        else "Low Risk"
    )

    return {
        "business_summary": {
            "total_revenue": float(total_revenue),
            "total_expense": float(total_expense),
            "profit": float(profit),
            "financial_health_score": score
        },
        "risk_overview": {
            "risk_level": risk_level
        },
        "industry_comparison": {
            "industry": industry
        },
        "investor_note": "Business is stable but requires cost optimization before scaling."
    }
