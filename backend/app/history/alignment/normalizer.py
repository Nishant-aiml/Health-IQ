# --------------------------------------------------
# File: normalizer.py
# Purpose: Biomarker Alignment Normalizer orchestrating canonical name resolution and unit harmonization.
# Module: Biomarker Alignment Engine / Normalizer
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from backend.app.history.alignment.models import AlignedBiomarker
from backend.app.history.alignment.matcher import biomarker_matcher
from backend.app.history.alignment.units import unit_harmonizer


class AlignmentNormalizer:
    """Orchestrates canonical matching and unit harmonization for historical biomarker readings."""

    def align_parameter(self, raw_name: str, value: float, unit: str) -> AlignedBiomarker:
        canonical_name = biomarker_matcher.match_canonical(raw_name)
        harm_val, harm_unit, is_harm = unit_harmonizer.harmonize_unit(canonical_name, value, unit)

        return AlignedBiomarker(
            raw_name=raw_name,
            canonical_name=canonical_name,
            value=harm_val,
            unit=harm_unit,
            original_value=value,
            original_unit=unit,
            is_harmonized=is_harm,
        )


alignment_normalizer = AlignmentNormalizer()
