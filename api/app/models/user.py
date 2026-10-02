from pydantic import BaseModel, ConfigDict


class UserRead(BaseModel):
    first_name: str
    last_name: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    first_name: str
    last_name: str