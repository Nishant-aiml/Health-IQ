# Core Configuration & Infrastructure (`backend/app/core/`)

## What is this folder?
This folder contains foundational cross-cutting concerns for the application:
- **`config/`**: Pydantic BaseSettings & application constants.
- **`logging.py`**: Centralized structured JSON logger.
- **`exceptions.py`**: Custom exception taxonomy and global HTTP exception handlers.
- **`middleware.py`**: Processing duration timer (`X-Process-Time`) and Request ID middleware.
- **`security/`**: CORS setup and HTTP security headers.

## Why does it exist?
Core infrastructure must remain isolated from domain logic so environment variables, security headers, logging formatting, and exception handling behave consistently across all current and future modules.
