from os import environ
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    """
    Set up application Config, env vars retrieved from docker container and fallback to their dev values
    """

    app_name: str = "API"
    env: str = environ.get("ENV", "development")
    db_user: str = ""
    db_password: str = ""
    db_file_name: str = "test.db"

    @property
    def db_url(self) -> str:
        """
        Build the url to the database
        """
        db_path = BASE_DIR / self.db_file_name
        url: str = environ.get("DATABASE_URL", f"sqlite:///{db_path.as_posix()}")
        return url


config = Config()
