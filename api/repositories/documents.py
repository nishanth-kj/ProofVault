from sqlalchemy.orm import Session
from api.models.document import Document
from typing import Optional, List, Dict, Any

class DocumentRepository:
    def get(self, db: Session, document_id: int) -> Optional[Document]:
        return db.query(Document).filter(Document.document_id == document_id).first()

    def get_by_hash(self, db: Session, document_hash: str) -> Optional[Document]:
        return db.query(Document).filter(Document.document_hash == document_hash).first()

    def create(self, db: Session, *, obj_in: Dict[str, Any]) -> Document:
        db_obj = Document(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Document]:
        return db.query(Document).offset(skip).limit(limit).all()

document_repo = DocumentRepository()
