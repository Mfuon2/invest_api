import logging
from logging.config import dictConfig

from fastapi import FastAPI

from app.configs.logger import LogConfig
from app.controllers.investor_controller import router as investor_router
from app.db.session import init_db

app = FastAPI(title='Invest', description='Description comes here', version='1.0')

app.include_router(investor_router)
dictConfig(LogConfig().dict())
log = logging.getLogger("logger")


@app.on_event("startup")
async def on_startup():
    log.info(f'Application Starting...')
    await init_db()


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     log.error(exc.json())
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"data": exc.errors(), "Error": "Name field is missing"}),
#     )
