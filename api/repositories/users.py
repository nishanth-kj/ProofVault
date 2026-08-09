from typing import Any

from models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    def get(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.user_id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: dict[str, Any]) -> User:
        db_obj = User(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()

user_repo = UserRepository()
