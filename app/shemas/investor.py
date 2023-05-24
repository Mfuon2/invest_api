from typing import Optional

from pydantic import BaseModel


class InvestorBase(BaseModel):
    id: Optional[int]
    fullname: str
    email: str


class InvestorCreate(InvestorBase):
    mobile: str


class InvestorUpdate(InvestorBase):
    pass


class InvestorRead(InvestorBase):
    id: int

    class Config:
        orm_mode = True
