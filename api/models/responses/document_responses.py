from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class DocumentResponse(BaseModel):
    id: int
    document_hash: str
    owner_id: int
    organization_id: int
    is_revoked: bool
    blockchain_tx_id: Optional[str] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class VerificationResponse(BaseModel):
    status: str
    message: str
