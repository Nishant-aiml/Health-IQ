# --------------------------------------------------
# File: units.py
# Purpose: Unit Harmonizer converting non-standard lab units to standardized baseline units prior to trend detection.
# Module: Biomarker Alignment Engine / Units
# Used By: Alignment Normalizer & Trend Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Tuple


class UnitHarmonizer:
    """Harmonizes non-standard biomarker measurement units."""

    def harmonize_unit(self, canonical_name: str, value: float, unit: str) -> Tuple[float, str, bool]:
        u_clean = unit.lower().strip()

        # Fasting Blood Sugar / Glucose: mmol/L -> mg/dL (multiplier: 18.018)
        if "Glucose" in canonical_name or "Blood Sugar" in canonical_name:
            if u_clean in ["mmol/l", "mmol/L"]:
                return round(value * 18.018, 1), "mg/dL", True

        # Total / HDL / LDL Cholesterol / Triglycerides: mmol/L -> mg/dL (multiplier: 38.67)
        if "Cholesterol" in canonical_name or "Triglycerides" in canonical_name:
            if u_clean in ["mmol/l", "mmol/L"]:
                return round(value * 38.67, 1), "mg/dL", True

        # Serum Creatinine: umol/L -> mg/dL (divider: 88.4)
        if "Creatinine" in canonical_name:
            if u_clean in ["umol/l", "µmol/l"]:
                return round(value / 88.4, 2), "mg/dL", True

        # Hemoglobin: g/L -> g/dL (divider: 10.0)
        if "Hemoglobin" in canonical_name:
            if u_clean in ["g/l"]:
                return round(value / 10.0, 1), "g/dL", True

        return value, unit, False


unit_harmonizer = UnitHarmonizer()
