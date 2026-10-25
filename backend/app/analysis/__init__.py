# --------------------------------------------------
# File: __init__.py
# Purpose: Analysis package index exporting Phase 2A and Phase 2B functions.
# Module: Analysis Engine
# Used By: Worker Queue Jobs & Report Services
# Future Phase: Phase 2A & 2B
# --------------------------------------------------

from backend.app.analysis.canonical import (
    resolve_canonical_name,
    normalize_unit,
    is_physiologically_plausible,
)
from backend.app.analysis.parser import normalize_report_data
from backend.app.analysis.demographic_ranges import get_demographic_normal_range
from backend.app.analysis.severity import evaluate_parameter_severity
from backend.app.analysis.critical_alerts import evaluate_critical_alerts
from backend.app.analysis.health_score import calculate_health_score
from backend.app.analysis.patterns import pattern_registry

__all__ = [
    "resolve_canonical_name",
    "normalize_unit",
    "is_physiologically_plausible",
    "normalize_report_data",
    "get_demographic_normal_range",
    "evaluate_parameter_severity",
    "evaluate_critical_alerts",
    "calculate_health_score",
    "pattern_registry",
]
