from tortoise.contrib.pydantic import pydantic_model_creator

from app.configs.custom_response import get_success
from app.models.models import Investor

investor_dto = pydantic_model_creator(Investor)
create_dto = pydantic_model_creator(Investor, exclude_readonly=True)


async def get_investor_service():
    results = await investor_dto.from_queryset(Investor.all())
    return get_success('Success', results)


async def create_investor_service(acc: create_dto):
    resp = await Investor.create(**acc.dict(exclude_unset=True))
    return get_success('Investor created successfully', await investor_dto.from_tortoise_orm(resp))


async def get_investor_by_id_service(account_id: str):
    results = await investor_dto.from_queryset_single(Investor.get(id=account_id))
    return get_success('Successfully loaded investors', results)


async def update_investor_service(investor_id: str, acc: create_dto):
    await Investor.filter(id=investor_id).update(**acc.dict(exclude_unset=True))
    results = await investor_dto.from_queryset_single(Investor.get(id=investor_id))
    return get_success('Success', results)
