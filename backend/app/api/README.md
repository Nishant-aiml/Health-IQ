# API Module (`backend/app/api/`)

## What is this folder?
This folder manages FastAPI route registration, versioned namespaces, and dependency injection providers.

## Why does it exist?
It acts as the entry interface for HTTP requests coming from the React frontend or external clients. It validates incoming parameters, injects database sessions and services, and delegates processing to business services.

## Contents
- **`dependencies.py`**: FastAPI dependency injection functions (`get_db_session()`, `get_health_service()`).
- **`v1/`**: Version 1 API routers (`/api/v1/`).

## Future Phases
Future AI, OCR, RAG, and QR sharing endpoints will register their controllers inside `v1/endpoints/`.
