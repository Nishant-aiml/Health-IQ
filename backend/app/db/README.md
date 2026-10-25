# Database Infrastructure (`backend/app/db/`)

## What is this folder?
This folder manages the database connection pool, engine configuration, table auto-creation hooks, and FastAPI session dependency generators.

## Why does it exist?
It isolates SQLite and SQLModel initialization logic (`session.py`) so repositories and endpoints can request a thread-safe database session without managing database creation or connection lifecycles directly.
