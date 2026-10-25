from typing import Optional
from sqlmodel import Session, select
from backend.app.models.user import User
from backend.app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def get_by_name(self, session: Session, name: str) -> Optional[User]:
        statement = select(User).where(User.name == name)
        return session.exec(statement).first()


user_repository = UserRepository()
