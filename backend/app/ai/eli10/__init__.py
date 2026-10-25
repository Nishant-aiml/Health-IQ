# --------------------------------------------------
# File: __init__.py
# Purpose: ELI10 package index.
# Module: AI Engine / ELI10
# Used By: Recommendation Service
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.eli10.generator import ELI10Generator, eli10_generator

__all__ = [
    "ELI10Generator",
    "eli10_generator",
]
