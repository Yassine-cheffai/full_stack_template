from fastapi import FastAPI

from api.v1.user import user_router
from core.config import config
from db.schema import Base, engine

ENV = config.app_env

Base.metadata.create_all(bind=engine)
app = FastAPI(title=config.app_name,
              docs_url="/docs" if ENV == "development" else None,
              redoc_url="/redoc" if ENV == "development" else None,
              openapi_url="/openapi.json" if ENV == "development" else None,
              )
app.include_router(user_router, prefix="/users")