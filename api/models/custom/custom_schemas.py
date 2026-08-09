from pydantic import BaseModel
from typing import Dict, Any

class CustomMetadata(BaseModel):
    key: str
    value: Any
