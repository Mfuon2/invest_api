from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float

from app.db.base import Base


class InvestorAccount(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String, index=True)
    units = Column(Float, default=0.00)
    unit_price = Column(Float, default=0.00)
    balance = Column(Float, default=0.00)
    contributions = Column(Float, default=0.00)
    cumulative_income = Column(Float, default=0.00)
    market_value = Column(Float, default=0.00)
    withdrawals = Column(Float, default=0.00)
    is_active = Column(Boolean)
    investor_id = Column(Integer, ForeignKey('investors.id'))
    investor_fund_id = Column(Integer, ForeignKey('funds.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


