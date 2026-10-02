from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from db.schema import SessionLocal
from models.user import UserRead, UserCreate
from services.user import UserService

user_router = APIRouter(tags=["User  Management"])


def create_user_service() -> UserService:
    """
    Create a service to manage users
    :return: UserService
    """
    return UserService(session=SessionLocal())


@user_router.get("/", response_model=list[UserRead])
async def users(user_service: UserService = Depends(create_user_service)) -> list[UserRead]:
    """
    Return a list of all users
    :return: list[UserRead]
    """
    return user_service.list_users()


@user_router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, user_service: UserService = Depends(create_user_service)) -> UserRead:
    """
    Return a user for a given user_id
    """
    result = user_service.get_user(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="User not found")

@user_router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, user_service: UserService = Depends(create_user_service)) -> UserRead:
    user_db = user_service.create_user(user)
    return user_db
