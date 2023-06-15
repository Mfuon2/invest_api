from typing import Any

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session, AsyncSession

from app.configs.custom_response import get_fail
from app.db.session import get_session, engine
from app.models.investor import Investor
from app.schemas.investor import InvestorCreate


async def get_one(investor_id: int, db: AsyncSession) -> Investor:
    investor = await db.execute(select(Investor).where(Investor.id == investor_id).limit(1))
    return investor.scalars().first()


async def create(investor: InvestorCreate, db: AsyncSession) -> Any:
    try:
        async with AsyncSession(engine) as db:
            investor_model = Investor( fullname=investor.fullname, email=investor.email, mobile=investor.mobile)
            db.add(investor_model)
            await db.commit()
            await db.refresh(investor_model)
            return investor_model
    except Exception as e:
        raise Exception(f"Failed to create user exception : {e.__dict__.get('orig')}")
