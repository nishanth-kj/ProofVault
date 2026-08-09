from sqlalchemy.orm import Session
from api.models.organization import Organization
from typing import Optional, List, Dict, Any

class OrganizationRepository:
    def get(self, db: Session, organization_id: int) -> Optional[Organization]:
        return db.query(Organization).filter(Organization.organization_id == organization_id).first()

    def get_by_name(self, db: Session, name: str) -> Optional[Organization]:
        return db.query(Organization).filter(Organization.name == name).first()

    def create(self, db: Session, *, obj_in: Dict[str, Any]) -> Organization:
        db_obj = Organization(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Organization]:
        return db.query(Organization).offset(skip).limit(limit).all()

organization_repo = OrganizationRepository()
