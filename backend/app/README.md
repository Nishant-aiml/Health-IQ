# Backend Application Core (`backend/app/`)

## What is this folder?
This folder contains the core Python FastAPI application logic, including database session handling, entity models, data access repositories, business services, configuration management, utility helpers, and REST API controllers.

## Why does it exist?
It enforces **Clean Architecture** by strictly separating application responsibilities:
- **`api/`**: HTTP Request controllers & dependency injection.
- **`core/`**: Configuration, logging, exception handlers, and security middleware.
- **`db/`**: Database connection pool & session factory.
- **`models/`**: SQLModel database entities.
- **`schemas/`**: Pydantic HTTP request/response validation objects.
- **`repositories/`**: Database queries & data access abstraction.
- **`services/`**: Core business domain logic engines.
- **`utils/`**: Shared helper functions (hashing, file validation, date formatting).

## Which modules use it?
All API endpoints, test suites, background workers, and future AI/RAG modules consume `backend/app/`.

## Which future phases will add to it?
- **Phase 2**: Adds `ocr/` module (Sarvam/Docling), `analysis/` module (severity/ranges), and `rag/` module (FAISS/BM25).
- **Phase 3**: Adds `prescriptions/` explainer and `trends/` timeline calculator.
- **Phase 5**: Adds `share/` QR generator service.
