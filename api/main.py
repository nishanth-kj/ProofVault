from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
from api.routes import documents
from api.utils.logger import logger

app = FastAPI(
    title="ProofVault API",
    description="Enterprise Blockchain Document Verification SaaS API",
    version="1.0.0"
)

class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(f"API Request: {request.method} {request.url.path} completed in {process_time:.4f}s with status {response.status_code}")
        return response

# Add Middleware
app.add_middleware(RequestTimingMiddleware)

# Include Routers
app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])

@app.on_event("startup")
async def startup_event():
    logger.info("ProofVault API is starting up...")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to ProofVault API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
