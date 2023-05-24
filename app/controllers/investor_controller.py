from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from app.configs.custom_response import get_success
from app.db.session import get_session
from app.services.investor_service import get_investor, create_investor
from app.shemas.investor import InvestorCreate, InvestorRead

router = APIRouter(prefix='/investor', tags=['Investor'])


@router.get(
    "/{investor_id}",
    response_model=InvestorRead,
)
async def get(investor_id: int, db: AsyncSession = Depends(get_session)):
    return await get_investor(investor_id, db)


@router.post("/create")
async def create(investor: InvestorCreate, db: AsyncSession = Depends(get_session)):
    created = await create_investor(investor, db)
    return created
