# API Schemas (`backend/app/schemas/`)

## What is this folder?
This folder defines Pydantic request and response models used by the API layer.

## Why does it exist?
To enforce strict boundary separation between external API JSON contracts (`schemas/`) and internal database entities (`models/`).

## Contents
- **`base.py`**: Standardized wrapper `BaseResponse` and `ErrorResponse`.
- **`health.py`**: `HealthStatus` schema.
- **`version.py`**: `VersionInfo` schema.
- **`report.py`**: Document upload & status responses.
- **`chat.py`**: RAG chat request/response models.
