
from pydantic import BaseModel


class DocumentCreateRequest(BaseModel):
    document_hash: str
    owner_id: int
    organization_id: int
    is_revoked: bool = False
    blockchain_tx_id: str | None = None
