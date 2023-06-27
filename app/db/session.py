import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from tortoise.contrib.fastapi import register_tortoise

from app.db.base import Base

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")
# engine = create_async_engine(DATABASE_URL, echo=True, future=True)


# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit=False,
#                                  autoflush=False)
#     async with async_session() as session:
#         yield session


