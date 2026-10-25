# --------------------------------------------------
# File: units.py
# Purpose: Unit conversion and standardization utilities for lab parameters.
# Module: Analysis Engine / Canonical Dictionary
# Used By: Report Normalizer
# Future Phase: Phase 2A Parsing
# --------------------------------------------------

from typing import Tuple


def normalize_unit(canonical_name: str, raw_value: float, raw_unit: str) -> Tuple[float, str]:
    """
    Standardizes laboratory units to canonical baseline units.

    Why it exists:
        Lab reports from different regions express parameters in different units
        (e.g., Blood Sugar in mg/dL vs mmol/L). Normalizing units guarantees correct
        downstream range comparisons.

    Inputs:
        canonical_name: Standardized parameter name.
        raw_value: Extracted numerical value.
        raw_unit: Extracted unit string.

    Returns:
        Tuple of (normalized_float_value, canonical_unit_string).
    """
    unit_cleaned = raw_unit.strip().lower()

    # Fasting Glucose conversion: mmol/L to mg/dL (1 mmol/L = 18.0182 mg/dL)
    if canonical_name == "Fasting Blood Sugar" and unit_cleaned in ["mmol/l", "mmol/L"]:
        return round(raw_value * 18.0182, 1), "mg/dL"

    # Cholesterol conversion: mmol/L to mg/dL (1 mmol/L = 38.67 mg/dL)
    if "Cholesterol" in canonical_name and unit_cleaned in ["mmol/l", "mmol/L"]:
        return round(raw_value * 38.67, 1), "mg/dL"

    # Creatinine conversion: umol/L to mg/dL (1 umol/L = 0.0113 mg/dL)
    if canonical_name == "Serum Creatinine" and unit_cleaned in ["umol/l", "µmol/l"]:
        return round(raw_value * 0.0113, 2), "mg/dL"

    return raw_value, raw_unit
