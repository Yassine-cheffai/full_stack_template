from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from api.v1.user import user_router
from core.config import config
from core.logging import setup_logging
from core.admin import setup_admin

ENV = config.env

setup_logging()

app = FastAPI(
    title=config.app_name,
    docs_url="/docs" if ENV == "development" else None,
    redoc_url="/redoc" if ENV == "development" else None,
    openapi_url="/openapi.json" if ENV == "development" else None,
)
app.include_router(user_router, prefix="/api/v1/users")

Instrumentator().instrument(app).expose(app)

setup_admin(app)
