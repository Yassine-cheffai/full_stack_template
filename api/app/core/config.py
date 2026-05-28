from pydantic_settings import BaseSettings


class Config(BaseSettings):
    app_name: str = "web for industry"
    db_user: str = ""
    db_password: str = ""
    db_name: str = "test.db"
    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"

config = Config()
