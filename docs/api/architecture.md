# API Architecture

ProofVault follows a strictly separated, Domain-Driven Design (DDD) inspired Clean Architecture.

## Backend (FastAPI)

The Python backend is structured to enforce strong boundaries between the database, business logic, and routing layers.

### 1. Database Models (`api/models/`)
- **Strict Separation**: Each database table is defined in its own individual file (e.g., `user.py`, `organization.py`, `document.py`).
- **No Shared Base**: The `Base = declarative_base()` is defined inline inside each model file. There is no global or shared `base.py` file.
- **Primary Keys**: We use simple, auto-incrementing integer primary keys named after the table (e.g., `organization_id`, `user_id`, `document_id`).
- **Audit Columns**: Every model includes `status`, `created_at`, `updated_at`, `created_by`, and `updated_by`. Timestamps are stored as Unix `BigInteger` milliseconds.

### 2. Repositories (`api/repositories/`)
- **No Generic Repositories**: Every repository explicitly writes out its own SQLAlchemy queries (`get`, `create`, `get_multi`, etc.). We do not use inheritance or generic `BaseRepository` abstractions to ensure full control over query execution.
- **Responsibility**: Repositories are the *only* place where `db.query()` is called. 

### 3. Services (`api/services/`)
- Business logic lives here. Services call Repositories to fetch/mutate data and apply rules (e.g., validating permissions before hashing a document).

### 4. Routes (`api/routes/`)
- FastAPI endpoints. Routes handle HTTP requests/responses, payload validation (Pydantic), and delegate logic to the Services.

### 5. Utilities (`api/utils/` & `api/constants/`)
- Contains centralized logging (`api/utils/logger.py`), time helpers (`api/utils/time_utils.py`), and constants (`api/constants/status.py` using a custom `IntEnum` pattern to support human-readable titles).
