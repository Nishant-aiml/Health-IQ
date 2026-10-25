# --------------------------------------------------
# File: __init__.py
# Purpose: Analysis config package index.
# Module: Analysis Engine / Config
# Used By: Severity & Health Score Calculators
# Future Phase: Phase 2B
# --------------------------------------------------

from backend.app.analysis.config.severity_thresholds import SEVERITY_THRESHOLDS
from backend.app.analysis.config.score_penalties import SEVERITY_PENALTIES, MAX_TOTAL_PENALTY

__all__ = [
    "SEVERITY_THRESHOLDS",
    "SEVERITY_PENALTIES",
    "MAX_TOTAL_PENALTY",
]
