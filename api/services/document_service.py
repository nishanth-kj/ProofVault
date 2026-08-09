from models.schemas import Document, DocumentCreate
from sqlalchemy.orm import Session

from constants.errors import ERROR_DOCUMENT_NOT_FOUND
from repositories.documents import document_repo
from utils.hash import generate_sha256_hash


class DocumentService:
    @staticmethod
    def verify_document(db: Session, file_bytes: bytes) -> dict:
        """
        Verifies a document by generating its SHA-256 hash and checking the database/blockchain.
        """
        document_hash = generate_sha256_hash(file_bytes)
        
        # Check against local DB first
        db_doc = document_repo.get_by_hash(db, document_hash)
        
        if not db_doc:
            return {"status": "Invalid", "message": ERROR_DOCUMENT_NOT_FOUND}
            
        if db_doc.is_revoked:
            return {"status": "Revoked", "message": "This document has been revoked."}
            
        # TODO: Check against Solana Blockchain using db_doc.blockchain_tx_id
        
        return {"status": "Verified", "message": "Document is authentic."}
        
    @staticmethod
    def issue_document(db: Session, doc_in: DocumentCreate) -> Document:
        """
        Issues a new document and saves it to the database.
        """
        return document_repo.create(db, obj_in=doc_in.model_dump())
