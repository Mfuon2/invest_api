from typing import Any

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.custom_response import get_success, get_fail, upsert_success
from app.repositories.investor_repository import get_one, create
from app.shemas.investor import InvestorRead, InvestorCreate


async def get_investor(investor_id: int, db: AsyncSession) -> Any:
    try:
        investor = await get_one(investor_id, db)
        return get_success('Successfully loaded investor', investor)
    except Exception as e:
        return get_fail(f"Request failed for user {investor_id} with exception {e}")


async def create_investor(investor: InvestorCreate, db: AsyncSession) -> Any:
    try:
        created = await create(investor, db)
        investor = InvestorRead(
            id=created.id,
            fullname=created.fullname,
            email=created.email,
            mobile=created.mobile
        )
        return upsert_success('Successfully created investor', investor)
    except Exception as e:
        return get_fail(f"Request failed with exception {e}")

