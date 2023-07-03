from typing import List

from fastapi import APIRouter

from app.services.investors import investor_dto, get_investor_service, create_dto, create_investor_service, \
    get_investor_by_id_service, update_investor_service

investor_routes = APIRouter(prefix='/investor', tags=['Investors'])


@investor_routes.get('/all', response_model=List[investor_dto])
async def get_investor():
    return await get_investor_service()


@investor_routes.post('/create', response_model=investor_dto)
async def create_investor(account: create_dto):
    return await create_investor_service(account)


@investor_routes.get('/{investor_id}')
async def get_investor_by_id(investor_id: str):
    return await get_investor_by_id_service(investor_id)


@investor_routes.put('/{investor_id}')
async def update_investor(investor_id: str, acc: create_dto):
    return await update_investor_service(investor_id, acc)
