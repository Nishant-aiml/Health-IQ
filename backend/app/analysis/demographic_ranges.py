# --------------------------------------------------
# File: demographic_ranges.py
# Purpose: Evaluates demographic-adjusted normal reference ranges for lab parameters.
# Module: Analysis Engine
# Used By: Parameter Severity Evaluator & Range Comparer
# Future Phase: Phase 2A Range Comparison & Phase 2B Severity
# --------------------------------------------------

from typing import Dict, Tuple, Optional


def get_demographic_normal_range(
    canonical_name: str,
    age: int = 30,
    gender: str = "male",
    pregnant: bool = False,
) -> Tuple[Optional[float], Optional[float]]:
    """
    Returns demographic-adjusted (low, high) normal reference range for a parameter.

    Why it exists:
        Several key parameters (Hemoglobin, Creatinine, TSH, Ferritin) have significantly
        different clinical normal ranges based on gender, age, and pregnancy status.
        Generic static range tables introduce medical inaccuracies.

    Inputs:
        canonical_name: Canonical lab parameter name.
        age: Patient age in years.
        gender: "male", "female", or "other".
        pregnant: Boolean pregnancy status.

    Returns:
        Tuple of (low_bound, high_bound) normal reference range values.
    """
    gender_clean = gender.lower()

    # Hemoglobin (g/dL)
    if canonical_name == "Hemoglobin":
        if pregnant:
            return (11.0, 14.0)
        elif gender_clean == "female":
            return (12.0, 15.5)
        else:
            return (13.8, 17.2)

    # Fasting Blood Sugar (mg/dL)
    if canonical_name == "Fasting Blood Sugar":
        return (70.0, 99.0)

    # Total Cholesterol (mg/dL)
    if canonical_name == "Total Cholesterol":
        return (125.0, 199.0)

    # Triglycerides (mg/dL)
    if canonical_name == "Triglycerides":
        return (40.0, 149.0)

    # Serum Creatinine (mg/dL)
    if canonical_name == "Serum Creatinine":
        if gender_clean == "female":
            return (0.59, 1.04)
        else:
            return (0.74, 1.35)

    # White Blood Cell Count (x10^3 /uL)
    if canonical_name == "White Blood Cell Count":
        return (4.5, 11.0)

    # Platelet Count (x10^3 /uL)
    if canonical_name == "Platelet Count":
        return (150.0, 450.0)

    # Thyroid Stimulating Hormone (mIU/L)
    if canonical_name == "Thyroid Stimulating Hormone":
        if pregnant:
            return (0.2, 2.5)
        return (0.45, 4.5)

    # Default fallback generic range
    return (None, None)
