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
        """
        query = Select(User)
        result = self._db.execute(query)
        users = result.scalars().all()
        users = [UserRead.model_validate(user) for user in users]
        logger.warning("list of users retrieved successfully")
        return users

    def get_user(self, user_id: int) -> UserRead | None:
        """
        Retrieve a user from DB by id, convert it to Data Transfer Object and return it, return `None` if user does not exist
        """
        assert isinstance(user_id, int), "user_id must be an int"
        try:
            query = Select(User).filter_by(id=user_id)
            result = self._db.execute(query)
            user = result.scalar_one_or_none()
            if not user:
                return None            
            return UserRead.model_validate(user)
        except Exception as e:
            logger.error(e)
            return None

    def create_user(self, user: UserCreate) -> UserRead:
        """
        Create a user, convert the user created to DTO and return it
        :param user: UserCreate
        :return: UserRead
        """
        assert isinstance(user, UserCreate), "user must be of type UserCreate"
        new_user = User(first_name=user.first_name, last_name=user.last_name)
        self._db.add(new_user)
        self._db.commit()
        self._db.refresh(new_user)
        return UserRead.model_validate(new_user)
