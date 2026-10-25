# --------------------------------------------------
# File: variability.py
# Purpose: Biomarker variability index calculator (Coefficient of Variation % = std_dev / mean * 100).
# Module: Time-Series Analytics / Variability
# Used By: Statistics Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Tuple


def calculate_variability(mean: float, std_dev: float) -> Tuple[float, str]:
    """Calculates Coefficient of Variation percentage and categorizes variability level."""
    if mean == 0:
        return 0.0, "LOW"
    cv = round((std_dev / abs(mean)) * 100, 1)

    if cv > 25.0:
        level = "HIGH"
    elif cv > 10.0:
        level = "MODERATE"
    else:
        level = "LOW"

    return cv, level
