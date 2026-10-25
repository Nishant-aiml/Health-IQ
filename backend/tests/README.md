# Backend Test Suite (`backend/tests/`)

## What is this folder?
This folder contains automated unit and integration test suites executed with Pytest.

## Why does it exist?
To guarantee application stability, API response correctness, CORS security, database session lifecycles, and exception handling logic:
- **`conftest.py`**: In-memory SQLite fixtures and FastAPI test client.
- **`test_health.py`**: Tests `/api/v1/health` endpoint.
- **`test_version.py`**: Tests `/api/v1/version` endpoint.
- **`test_db.py`**: Tests SQLModel table creation and record insertion.
- **`test_cors.py`**: Tests CORS origin headers.
- **`test_exceptions.py`**: Tests custom exception handling and 404 responses.
