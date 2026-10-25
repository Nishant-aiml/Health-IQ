# Utility Helpers (`backend/app/utils/`)

## What is this folder?
This folder contains shared, side-effect-free helper utilities used across the backend.

## Why does it exist?
To avoid repeating utility code (file extensions, hashing, date formatting) across repositories and services:
- **`file_utils.py`**: Extension extraction, SHA-256 hash calculation, document type validation.
- **`datetime_utils.py`**: UTC timestamp generation and ISO-8601 formatting.
