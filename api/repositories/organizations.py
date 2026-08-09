from typing import Any

from sqlalchemy.orm import Session

from models.organization import Organization


class OrganizationRepository:
    def get(self, db: Session, organization_id: int) -> Organization | None:
        return db.query(Organization).filter(Organization.organization_id == organization_id).first()

    def get_by_name(self, db: Session, name: str) -> Organization | None:
        return db.query(Organization).filter(Organization.name == name).first()

    def create(self, db: Session, *, obj_in: dict[str, Any]) -> Organization:
        db_obj = Organization(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Organization]:
        return db.query(Organization).offset(skip).limit(limit).all()

organization_repo = OrganizationRepository()
