import logging
from sqlalchemy import Select
from sqlalchemy.orm import Session

from db.schema import User
from models.user import UserRead, UserCreate

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, session: Session):
        self._db = session

    def list_users(self) -> list[UserRead]:
        """
        Retrieve list of users from DB, convert them to DTOs / Data Transfer Objects and return them
        :return: list[UserRead]
        """
        query = Select(User)
        result = self._db.execute(query)
        users = result.scalars().all()
        users = [UserRead.model_validate(user) for user in users]
        logger.warn("list of users retrieved successfully")
        # breakpoint()
        return users

    def get_user(self, user_id: int) -> UserRead:
        """
        Retrieve a user from DB by id, convert it to Data Transfer Object and return it
        :param user_id: int
        :return: UserRead
        """
        assert isinstance(user_id, int), "user_id must be an int"
        query = Select(User).filter_by(id=user_id)
        result = self._db.execute(query)
        user = result.scalar_one_or_none()
        return UserRead.model_validate(user)

    def create_user(self, user: UserCreate) -> UserRead:
        """
        Create a user, convert the user created to DTO and return it
        :param user: UserCreate
        :return: UserRead
        """
        assert isinstance(user, UserCreate), "user must be of type UserCreate"
        new_user = User(name=user.name)
        self._db.add(new_user)
        self._db.commit()
        self._db.refresh(new_user)
        return UserRead.model_validate(new_user)
