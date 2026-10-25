# Domain Database Models (`backend/app/models/`)

## What is this folder?
This folder defines all SQLModel database entity schemas for the AI Health Intelligence Platform.

## Why does it exist?
Every domain entity lives in its own dedicated file to prevent monolithic files. SQLModel combines SQLAlchemy ORM table definitions with Pydantic validation:
- **`user.py`**: Patient profile (`users` table).
- **`report.py`**: Uploaded document metadata (`reports` table).
- **`extracted_value.py`**: Canonicalized lab parameters (`extracted_values` table).
- **`prescription.py`**: Parsed medications (`prescriptions` table).
- **`risk_analysis.py`**: Health score & pattern analysis (`risk_analysis` table).
- **`recommendation.py`**: Evidence & limitation structured output (`recommendations` table).
- **`doctor_question.py`**: Auto-generated doctor questions (`doctor_questions` table).
- **`job.py`**: Ingestion queue worker state (`jobs` table).
- **`chat.py`**: RAG chat sessions & message history (`chat_sessions`, `chat_messages` tables).
- **`guidelines.py`**: Vector embeddings corpus (`guidelines_corpus` table).
- **`trend.py`**: Denormalized parameter timeline (`trend_snapshots` table).
- **`share.py`**: Temporary QR profile sharing (`shared_profiles` table).

## Future Usage
All 13 tables are pre-configured in Phase 1 so subsequent OCR, RAG, and AI modules can store data without requiring complex schema migrations.
