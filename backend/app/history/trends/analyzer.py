# --------------------------------------------------
# File: analyzer.py
# Purpose: Trend Analyzer orchestrator converting historical series into TrendAnalysisResult objects.
# Module: Trend Detection Engine / Analyzer
# Used By: History Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.trends.models import TrendAnalysisResult
from backend.app.history.trends.rules import evaluate_trend_direction


class TrendAnalyzer:
    """Orchestrates deterministic trend classification."""

    def analyze_series(self, canonical_name: str, readings: List[HistoricalParameterReading]) -> TrendAnalysisResult:
        direction, confidence, pct_change, abs_change, evidence = evaluate_trend_direction(readings)
        unit = readings[-1].unit if readings else "mg/dL"

        # Generate safety-focused comparative summary without medical diagnosis
        first_val = readings[0].value if readings else 0.0
        last_val = readings[-1].value if readings else 0.0

        if direction == "recovery":
            summary = f"Compared with your previous report, {canonical_name} has improved into the normal reference range ({last_val} {unit})."
        elif direction == "persistent_abnormality":
            summary = f"Compared with previous reports, {canonical_name} has remained outside the reference range across consecutive readings."
        elif direction == "rapid_change":
            summary = f"Compared with your previous report, {canonical_name} shifted by {abs(pct_change)}% ({last_val} {unit})."
        elif direction == "increasing":
            summary = f"Compared with your initial baseline ({first_val} {unit}), {canonical_name} has increased to {last_val} {unit}."
        elif direction == "decreasing":
            summary = f"Compared with your initial baseline ({first_val} {unit}), {canonical_name} has decreased to {last_val} {unit}."
        else:
            summary = f"{canonical_name} has remained stable at {last_val} {unit}."

        return TrendAnalysisResult(
            canonical_name=canonical_name,
            unit=unit,
            direction=direction,
            trend_confidence=confidence,
            available_reports=len(readings),
            required_reports=2,
            percentage_change=pct_change,
            absolute_change=abs_change,
            evidence=evidence,
            clinical_summary=summary,
        )


trend_analyzer = TrendAnalyzer()
