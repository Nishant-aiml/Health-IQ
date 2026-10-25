# --------------------------------------------------
# File: __init__.py
# Purpose: Evidence package index.
# Module: AI Engine / Evidence
# Used By: Recommendation Service
# Future Phase: Phase 2C
# --------------------------------------------------

from backend.app.ai.evidence.builder import EvidenceBuilder, evidence_builder

__all__ = [
    "EvidenceBuilder",
    "evidence_builder",
]
