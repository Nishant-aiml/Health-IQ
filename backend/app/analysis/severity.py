# --------------------------------------------------
# File: severity.py
# Purpose: Parameter deviation severity evaluator.
# Module: Analysis Engine
# Used By: Worker Queue Jobs & Health Score Engine
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Optional
from backend.app.analysis.config.severity_thresholds import SEVERITY_THRESHOLDS


def evaluate_parameter_severity(
    canonical_name: str,
    value: float,
    low_bound: Optional[float],
    high_bound: Optional[float],
) -> str:
    """
    Evaluates severity level of a lab parameter value against demographic-adjusted normal ranges.

    Why it exists:
        Categorizes values into `normal`, `mild`, `moderate`, `severe` based on percentage deviation
        from normal range midpoint.

    Inputs:
        canonical_name: Canonical lab parameter string.
        value: Extracted numerical value.
        low_bound: Normal range low baseline.
        high_bound: Normal range high baseline.

    Returns:
        Severity level string: "normal", "mild", "moderate", or "severe".
    """
    if low_bound is None or high_bound is None:
        return "normal"

    if low_bound <= value <= high_bound:
        return "normal"

    # Specific Fasting Blood Sugar logic
    if canonical_name == "Fasting Blood Sugar":
        if value <= 125.0:
            return "mild"
        elif value <= 180.0:
            return "moderate"
        else:
            return "severe"

    # Percentage deviation calculation beyond midpoint
    range_midpoint = (low_bound + high_bound) / 2.0
    range_span = high_bound - low_bound if high_bound > low_bound else 1.0

    deviation_amount = abs(value - range_midpoint) - (range_span / 2.0)
    percent_deviation = (deviation_amount / range_span) * 100.0

    if percent_deviation <= SEVERITY_THRESHOLDS["default"]["mild_percent"]:
        return "mild"
    elif percent_deviation <= SEVERITY_THRESHOLDS["default"]["moderate_percent"]:
        return "moderate"
    else:
        return "severe"
