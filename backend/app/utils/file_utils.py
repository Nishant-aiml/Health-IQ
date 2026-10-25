# --------------------------------------------------
# File: file_utils.py
# Purpose: File helper utilities (extension validation, SHA-256 hashing).
# Module: Core Utilities
# Used By: Document Service & Ingestion Engine
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

import os
import hashlib


def get_file_extension(filename: str) -> str:
    """Returns the lowercased extension of a filename."""
    _, ext = os.path.splitext(filename)
    return ext.lower().lstrip(".")


def calculate_file_hash(file_bytes: bytes) -> str:
    """Calculates SHA-256 hash of raw file bytes."""
    return hashlib.sha256(file_bytes).hexdigest()


def is_supported_document_type(filename: str) -> bool:
    """Checks whether the file has a supported document extension (PDF/PNG/JPG/JPEG/DOCX/TXT)."""
    ext = get_file_extension(filename)
    if not ext:
        return True  # Allow raw pasted text files without extension
    return ext in {"pdf", "png", "jpg", "jpeg", "docx", "txt"}
