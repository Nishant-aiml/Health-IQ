# --------------------------------------------------
# File: matcher.py
# Purpose: Canonical biomarker matcher reusing Phase 2A canonical dictionary (Hb, Hemoglobin, HGB -> Hemoglobin).
# Module: Biomarker Alignment Engine / Matcher
# Used By: Alignment Normalizer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from backend.app.analysis.canonical import resolve_canonical_name


class BiomarkerMatcher:
    """Aligns raw parameter strings to single canonical parameter keys."""

    def match_canonical(self, raw_name: str) -> str:
        resolved = resolve_canonical_name(raw_name)
        if resolved:
            return resolved
        return raw_name.strip()


biomarker_matcher = BiomarkerMatcher()
