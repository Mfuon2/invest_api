from typing import Optional

from pydantic import BaseModel
from pydantic.schema import date, datetime


class InvestorBase(BaseModel):
    id: Optional[int]


class InvestorCreate(InvestorBase):
    mobile: str
    fullname: str
    email: str
    code = str
    identity = str
    identity_type = str
    date_of_birth = date
    created_at = datetime
    updated_at = datetime
    tax_number = str


class InvestorUpdate(InvestorBase):
    id: int


class InvestorRead(InvestorBase):
    id: int

    class Config:
        orm_mode = True
