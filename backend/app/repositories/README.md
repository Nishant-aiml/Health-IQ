# Data Repositories (`backend/app/repositories/`)

## What is this folder?
This folder contains the Repository Pattern data access layer for interacting with SQLModel database entities.

## Why does it exist?
It abstracts database query execution (SQL SELECT/INSERT/UPDATE/DELETE) away from business services and API controllers:
- **`base.py`**: Generic `BaseRepository[T]` providing CRUD operations.
- **`user_repository.py`**: Patient queries.
- **`report_repository.py`**: Document & status queries.
- **`job_repository.py`**: Asynchronous job lifecycle updates.
