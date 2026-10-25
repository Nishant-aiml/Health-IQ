# Business Service Layer (`backend/app/services/`)

## What is this folder?
This folder houses business logic service engines.

## Why does it exist?
Service components orchestrate business workflows, calculations, external service calls, and repository queries. Controllers invoke services rather than performing database operations directly:
- **`base.py`**: Base class for domain services.
- **`health_service.py`**: Evaluates system operational status and database connectivity.

## Future Services
Subsequent phases will introduce `ocr_service.py`, `analysis_service.py`, `rag_service.py`, `recommendation_service.py`, `prescription_service.py`, and `share_service.py`.
