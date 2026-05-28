from fastapi import FastAPI

from api.v1.user import  user_router
from core.config import config
from db.schema import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.app_name)

app.include_router(user_router, prefix="/users")