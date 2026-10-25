from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    """
    Generic CRUD Repository base class using SQLModel.
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, session: Session, id: int) -> Optional[ModelType]:
        return session.get(self.model, id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        return session.exec(statement).all()

    def create(self, session: Session, obj_in: ModelType) -> ModelType:
        session.add(obj_in)
        session.commit()
        session.refresh(obj_in)
        return obj_in

    def delete(self, session: Session, id: int) -> bool:
        obj = self.get_by_id(session, id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False
