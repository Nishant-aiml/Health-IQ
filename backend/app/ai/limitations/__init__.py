# --------------------------------------------------
# File: __init__.py
# Purpose: Limitations package index.
# Module: AI Engine / Limitations
# Used By: Recommendation Service
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.limitations.generator import LimitationsGenerator, limitations_generator

__all__ = [
    "LimitationsGenerator",
    "limitations_generator",
]
