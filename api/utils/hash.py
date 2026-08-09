import hashlib


def generate_sha256_hash(data: bytes) -> str:
    """
    Generates a SHA-256 hash for the given data (e.g., a PDF document).
    """
    return hashlib.sha256(data).hexdigest()
