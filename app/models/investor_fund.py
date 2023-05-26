from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.address import Address
from app.models.investor_document import InvestorDocument


class InvestorFund(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String, index=True)
    early_withdrawal_penalty = Column(Float, default=0.00)
    fund_share_class_code = Column(String)
    guaranteed_interest_rate = Column(Float, default=0.00)
    maximum_contribution = Column(Float, default=0.00)
    maximum_withdrawal = Column(Float, default=150000.00)
    minimum_contribution = Column(Float, default=100.00)
    minimum_withdrawal = Column(Float, default=50.00)
    withdrawal_limit = Column(Float, default=0.00)
    withdrawal_limit_duration = Column(Integer, default=24)
    withdrawal_limit_duration_type = Column(String, default="HRS")
    withdrawal_settlement_period = Column(Integer, default=2)
    withdrawal_settlement_period_type = Column(String, default="Days")
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)



