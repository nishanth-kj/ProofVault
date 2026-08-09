import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ProofVault"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database & Redis
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/proofvault")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # Solana
    SOLANA_NETWORK: str = os.getenv("SOLANA_NETWORK", "devnet")
    SOLANA_RPC_URL: str = os.getenv("SOLANA_RPC_URL", "https://api.devnet.solana.com")
    ANCHOR_WALLET: str = os.getenv("ANCHOR_WALLET", "/path/to/wallet.json")

    class Config:
        env_file = ".env"

settings = Settings()
