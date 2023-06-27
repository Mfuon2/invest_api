from typing import List

from fastapi import APIRouter
from app.services.accounts import get_accounts_service, dto, createDto, create_accounts_service, \
    get_account_by_id_service, update_account_service

accounts_routes = APIRouter(prefix='/account', tags=['accounts'])


@accounts_routes.get('/all', response_model=List[dto])
async def get_accounts():
    return await get_accounts_service()


@accounts_routes.post('/create', response_model=dto)
async def create_account(account: createDto):
    return await create_accounts_service(account)


@accounts_routes.get('/{account_id}')
async def get_account_by_id(account_id: str):
    return await get_account_by_id_service(account_id)


@accounts_routes.put('/{account_id}')
async def update_account(account_id: str, acc: createDto):
    return await update_account_service(account_id, acc)
