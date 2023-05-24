from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.address import Address
from app.models.investor_account import InvestorAccount
from app.models.investor_document import InvestorDocument


class Investor(Base):
    __tablename__ = "investors"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    email = Column(String, index=True)
    mobile = Column(String, index=True)
    code = Column(String)
    identity = Column(String)
    identity_type = Column(String)
    date_of_birth = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    tax_number = Column(String)
    addresses = relationship(Address, cascade="all, delete-orphan", backref='investor_addresses')
    documents = relationship(InvestorDocument, cascade="all, delete-orphan", backref='investor_documents')
    accounts = relationship(InvestorAccount, cascade="all, delete-orphan", backref='investor_accounts')

