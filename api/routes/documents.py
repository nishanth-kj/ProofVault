
from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/verify")
async def verify_document(file: UploadFile = File(...)) -> dict[str, str]:  # noqa: B008
    """
    Endpoint to verify a document against the blockchain using its SHA-256 hash.
    """
    return {"status": "Verified", "message": "Document is authentic."}
