from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Double, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.address import Address
from app.models.investor_document import InvestorDocument


class Investor(Base):
    __tablename__ = "funds"

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

    id
    contribution_business_account
    created_at
    early_withdrawal_penalty
    fund_name
    fund_share_class_code
    guaranteed_interest_rate
    maximum_contribution
    maximum_withdrawal
    minimum_contribution
    minimum_withdrawal
    show_on_ussd
    unit_price
    updated_at
    withdrawal_limit
    withdrawal_limit_duration
    withdrawal_limit_duration_type
    withdrawal_settlement_period
    withdrawal_settlement_period_type



