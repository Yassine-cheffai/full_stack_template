from os import environ
from pathlib import Path

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Set up application Config, env vars retrieved from docker container and fallback to their dev values
    """
    app_name: str = "API"
    env: str = environ.get("ENV", "development")
    db_user: str = ""
    db_password: str = ""

    @property
    def db_url(self):
        base_dir = Path(__file__).resolve()
        url: str = environ.get("DATABASE_URL", "sqlite:///./test.db")
        return url


config = Config()
