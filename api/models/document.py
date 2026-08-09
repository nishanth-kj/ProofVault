from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base
from api.constants.status import Status
from api.utils.time_utils import current_milli_time

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    document_hash = Column(String, unique=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
    organization_id = Column(Integer, ForeignKey("organizations.organization_id"))
    blockchain_tx_id = Column(String, nullable=True)
    
    # Audit Columns
    status = Column(Integer, default=Status.ACTIVE.code)
    created_at = Column(BigInteger, default=current_milli_time)
    updated_at = Column(BigInteger, default=current_milli_time, onupdate=current_milli_time)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
