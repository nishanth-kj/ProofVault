# ProofVault API

This is the backend API for ProofVault, an Enterprise Blockchain Document Verification SaaS. 

## Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (for ultra-fast Python package management)

## Setup & Running the Project

1. **Navigate to the `api` directory** (if you aren't already there):
   ```bash
   cd api
   ```

2. **Run the API server**:
   We use `uv` to handle our environment. You can start the Uvicorn server simply by running:
   ```bash
   uv run python main.py
   ```
   *Note: This automatically adds the project root to your Python path, so all `api.*` imports will resolve correctly.*

3. **View Documentation**:
   Once running, you can access the interactive API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Version
The current simple version of this API is **1.0.0**.
