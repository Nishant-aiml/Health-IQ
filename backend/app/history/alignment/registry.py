# --------------------------------------------------
# File: registry.py
# Purpose: Biomarker Alignment Engine registry.
# Module: Biomarker Alignment Engine
# Used By: History Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.alignment.normalizer import alignment_normalizer, AlignmentNormalizer


class AlignmentRegistry:
    def align_parameter(self, raw_name: str, value: float, unit: str):
        return alignment_normalizer.align_parameter(raw_name, value, unit)


alignment_registry = AlignmentRegistry()
