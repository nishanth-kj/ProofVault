from typing import Any

from pydantic import BaseModel


class CustomMetadata(BaseModel):
    key: str
    value: Any
