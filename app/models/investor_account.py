from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Double, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.address import Address
from app.models.investor_document import InvestorDocument


class InvestorAccount(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String, index=True)
    units = Column(Double, default=0.00)
    unit_price = Column(Double, default=0.00)
    balance = Column(Double, default=0.00)
    contributions = Column(Double, default=0.00)
    cumulative_income = Column(Double, default=0.00)
    market_value = Column(Double, default=0.00)
    withdrawals = Column(Double, default=0.00)
    is_active = Column(Boolean)
    investor_id = Column(Integer, ForeignKey('investors.id'))
    investor_fund_id = Column(Integer, ForeignKey('investment_funds.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


