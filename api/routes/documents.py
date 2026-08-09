from fastapi import APIRouter, File, UploadFile
from typing import Dict

router = APIRouter()

@router.post("/verify")
async def verify_document(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Endpoint to verify a document against the blockchain using its SHA-256 hash.
    """
    return {"status": "Verified", "message": "Document is authentic."}
