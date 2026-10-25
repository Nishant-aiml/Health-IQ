# --------------------------------------------------
# File: validators.py
# Purpose: Parameter sanity and numeric bounds validation.
# Module: Analysis Engine / Canonical Dictionary
# Used By: Report Parser & Normalizer
# Future Phase: Phase 2A Parsing
# --------------------------------------------------

def is_physiologically_plausible(canonical_name: str, value: float) -> bool:
    """
    Validates whether an extracted numerical value falls within physiologically plausible bounds.

    Why it exists:
        Prevents OCR errors (e.g. extra decimal points or stray characters reading 1200 mg/dL as 12000 mg/dL)
        from corrupting analysis.

    Inputs:
        canonical_name: Canonical lab parameter name.
        value: Extracted numerical value.

    Returns:
        bool indicating whether the value is plausible.
    """
    if value < 0:
        return False

    bounds = {
        "Hemoglobin": (1.0, 30.0),
        "White Blood Cell Count": (0.1, 300.0),
        "Platelet Count": (1.0, 2000.0),
        "Fasting Blood Sugar": (10.0, 1500.0),
        "Total Cholesterol": (20.0, 1000.0),
        "Serum Creatinine": (0.1, 50.0),
        "Thyroid Stimulating Hormone": (0.001, 500.0),
    }

    if canonical_name in bounds:
        min_val, max_val = bounds[canonical_name]
        return min_val <= value <= max_val

    return True
