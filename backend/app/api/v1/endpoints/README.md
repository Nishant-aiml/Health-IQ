# API V1 Endpoints (`backend/app/api/v1/endpoints/`)

## What is this folder?
This folder holds individual endpoint controller files split by domain domain feature.

## Why does it exist?
To avoid monolithic API files and keep controllers focused on a single HTTP endpoint namespace:
- **`health.py`**: System health check (`GET /api/v1/health`).
- **`version.py`**: Application version info (`GET /api/v1/version`).
- **`documents.py`**: Document batch ingestion placeholder (`POST /api/v1/documents/batch`).
- **`reports.py`**: Report analysis placeholder (`GET /api/v1/reports/{id}`).
- **`prescriptions.py`**: Medicine explainer placeholder (`GET /api/v1/prescriptions/{id}`).
- **`chat.py`**: RAG grounded chat placeholder (`POST /api/v1/chat/{session_id}/message`).
- **`trends.py`**: Health parameter trend timeline placeholder (`GET /api/v1/trends/{user_id}`).
- **`share.py`**: Patient QR health card placeholder (`POST /api/v1/share`).

## Which future phases will add to it?
Phase 2 (Documents, Reports, Chat), Phase 3 (Prescriptions, Trends), and Phase 5 (Share) will populate these endpoints.
