from tortoise.contrib.pydantic import pydantic_model_creator

from app.configs.custom_response import get_success
from app.models.models import InvestorAccount

dto = pydantic_model_creator(InvestorAccount)
createDto = pydantic_model_creator(InvestorAccount, exclude_readonly=True)


async def get_accounts_service():
    results = await dto.from_queryset(InvestorAccount.all())
    return get_success('Success', results)


async def create_accounts_service(acc: createDto):
    resp = await InvestorAccount.create(**acc.dict(exclude_unset=True))
    return get_success('Account created successfully', await dto.from_tortoise_orm(resp))


async def get_account_by_id_service(account_id: str):
    results = await dto.from_queryset_single(InvestorAccount.get(id=account_id))
    return get_success('Success', results)


async def update_account_service(account_id: str, acc: createDto):
    await InvestorAccount.filter(id=account_id).update(**acc.dict(exclude_unset=True))
    results = await dto.from_queryset_single(InvestorAccount.get(id=account_id))
    return get_success('Success', results)
