import logging
from logging.config import dictConfig

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import BaseORMException, ValidationError

from app.configs.custom_response import get_fail
from app.configs.logger import LogConfig
from app.controllers.accounts_controller import accounts_routes
from app.controllers.investor_controller import investor_routes
from app.db.session import DATABASE_URL

app = FastAPI(title='Invest', description='Description comes here', version='1.0')
app.include_router(investor_routes)
app.include_router(accounts_routes)
dictConfig(LogConfig().dict())
log = logging.getLogger("logger")


@app.on_event("startup")
async def on_startup():
    log.info(f'Application Starting...')
    # await init_db()


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models":
        [
            "app.models.models"
        ]
    },

    generate_schemas=True,
    add_exception_handlers=True,
)
