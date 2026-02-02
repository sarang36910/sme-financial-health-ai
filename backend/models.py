from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class FinancialReport(Base):
    __tablename__ = "financial_reports"

    id = Column(Integer, primary_key=True, index=True)
    industry = Column(String)
    total_revenue = Column(Float)
    total_expense = Column(Float)
    profit = Column(Float)
    health_score = Column(Integer)
    insight = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
