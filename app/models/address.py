from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.db.base import Base


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    physical_address = Column(String)
    postal_address = Column(String)
    investor_id = Column(Integer, ForeignKey('investors.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


