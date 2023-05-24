from typing import Any

from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse


def get_success(message: str, data: Any):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"message": message, "success": True, "data": data}),
    )


def upsert_success(message: str, data: Any):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({"message": message, "success": True, "data": data}),
    )


def get_fail(message: str):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"message": message, "success": False}),
    )
