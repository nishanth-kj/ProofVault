# API Setup Guide

We use `uv` for ultra-fast Python environment and package management.

### 1. Environment Setup

Copy the environment example file and adjust it for your local machine:
```bash
cp api/.env.example api/.env
```
*(Or simply create your own `.env` file based on `.env.example`)*

### 2. Dependency Installation

Navigate to the `api` directory and install the requirements via `uv`:
```bash
cd api
uv venv
uv pip install -r requirements.txt
```

### 3. Database Migrations (Alembic)

Alembic is configured to handle database migrations.
- To generate a new migration after updating a model: `uv run alembic revision --autogenerate -m "message"`
- To apply migrations to the database: `uv run alembic upgrade head`

### 4. Running the Server

Run the FastAPI application locally with auto-reload:
```bash
cd api
uv run uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`. You can view the auto-generated Swagger UI docs at `http://localhost:8000/docs`.
