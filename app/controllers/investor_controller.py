from fastapi import APIRouter

investor_routes = APIRouter(prefix='/investor', tags=['Investor'])


# @investor_routes.get("/all")
# async def get_investors():
#     pass
