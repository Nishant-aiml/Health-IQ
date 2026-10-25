# --------------------------------------------------
# File: __init__.py
# Purpose: Canonical package index.
# Module: Analysis Engine / Canonical Dictionary
# Used By: Report Parser
# Future Phase: Phase 2A
# --------------------------------------------------

from backend.app.analysis.canonical.aliases import resolve_canonical_name, CANONICAL_ALIASES
from backend.app.analysis.canonical.units import normalize_unit
from backend.app.analysis.canonical.validators import is_physiologically_plausible

__all__ = [
    "resolve_canonical_name",
    "CANONICAL_ALIASES",
    "normalize_unit",
    "is_physiologically_plausible",
]
