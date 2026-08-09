from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base
from api.constants.status import Status
from api.utils.time_utils import current_milli_time

Base = declarative_base()

class Organization(Base):
    __tablename__ = "organizations"

    organization_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    
    # Audit Columns
    status = Column(Integer, default=Status.ACTIVE.code)
    created_at = Column(BigInteger, default=current_milli_time)
    updated_at = Column(BigInteger, default=current_milli_time, onupdate=current_milli_time)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
