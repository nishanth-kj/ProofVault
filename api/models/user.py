from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base
from api.constants.status import Status
from api.utils.time_utils import current_milli_time

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.organization_id"))
    role = Column(String)
    
    # Audit Columns
    status = Column(Integer, default=Status.ACTIVE.code)
    created_at = Column(BigInteger, default=current_milli_time)
    updated_at = Column(BigInteger, default=current_milli_time, onupdate=current_milli_time)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
