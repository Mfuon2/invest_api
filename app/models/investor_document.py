from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.db.base import Base


class InvestorDocument(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    document_type = Column(String)
    document_url = Column(String)
    investor_id = Column(Integer, ForeignKey('investors.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
