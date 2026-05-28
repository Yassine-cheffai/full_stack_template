from pydantic import BaseModel, ConfigDict


class UserRead(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str