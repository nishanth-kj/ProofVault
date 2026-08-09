from pydantic import BaseModel
from typing import Optional

class DocumentCreateRequest(BaseModel):
    document_hash: str
    owner_id: int
    organization_id: int
    is_revoked: bool = False
    blockchain_tx_id: Optional[str] = None
