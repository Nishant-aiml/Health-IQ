# --------------------------------------------------
# File: rules.py
# Purpose: Deterministic trend rules (Increasing, Decreasing, Stable, Rapid Change, Oscillation, Recovery, Persistent Abnormality).
# Module: Trend Detection Engine / Rules
# Used By: Trend Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Tuple
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.trends.models import TrendEvidence


def evaluate_trend_direction(readings: List[HistoricalParameterReading]) -> Tuple[str, str, float, float, TrendEvidence]:
    """
    Evaluates deterministic biomarker trend trajectory across historical readings.
    """
    count = len(readings)
    if count == 0:
        evidence = TrendEvidence(rule_triggered="NO_DATA", explanation="No historical readings available.")
        return "stable", "LOW", 0.0, 0.0, evidence

    report_dates = [r.collection_date for r in readings]
    values = [r.value for r in readings]
    first_val = values[0]
    last_val = values[-1]
    abs_change = round(last_val - first_val, 2)

    pct_change = 0.0
    if first_val != 0:
        pct_change = round(((last_val - first_val) / abs(first_val)) * 100, 1)

    confidence = "HIGH" if count >= 3 else "MEDIUM" if count == 2 else "LOW"

    # Single Report Edge Case
    if count == 1:
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="SINGLE_REPORT_BASELINE",
            explanation="Baseline single report reading recorded.",
        )
        return "stable", "LOW", 0.0, 0.0, evidence

    # Rule 1: Recovery (Was abnormal in previous, returned to normal in latest)
    prev_sev = readings[-2].severity
    last_sev = readings[-1].severity
    if prev_sev in ["ELEVATED", "LOW", "CRITICAL"] and last_sev == "NORMAL":
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="RECOVERY_TO_NORMAL_RANGE",
            explanation=f"Parameter returned into standard reference range ({last_val} {readings[-1].unit}).",
        )
        return "recovery", confidence, pct_change, abs_change, evidence

    # Rule 2: Persistent Abnormality (Abnormal in last 2+ consecutive reports)
    if prev_sev in ["ELEVATED", "LOW", "CRITICAL"] and last_sev in ["ELEVATED", "LOW", "CRITICAL"]:
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="PERSISTENT_ABNORMALITY",
            explanation=f"Parameter has remained outside standard reference range across consecutive reports.",
        )
        return "persistent_abnormality", confidence, pct_change, abs_change, evidence

    # Rule 3: Rapid Change (> 20% shift between adjacent readings)
    adjacent_pct = 0.0
    if values[-2] != 0:
        adjacent_pct = abs(((last_val - values[-2]) / abs(values[-2])) * 100)
    if adjacent_pct > 20.0:
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="RAPID_MAGNITUDE_SHIFT",
            explanation=f"Significant shift of {round(adjacent_pct, 1)}% detected between recent consecutive reports.",
        )
        return "rapid_change", confidence, pct_change, abs_change, evidence

    # Rule 4: Oscillation (Alternating direction across 3+ reports)
    if count >= 3:
        diffs = [values[i] - values[i - 1] for i in range(1, count)]
        signs = [1 if d > 0 else -1 if d < 0 else 0 for d in diffs]
        is_oscillating = any(signs[i] != signs[i - 1] and signs[i] != 0 and signs[i - 1] != 0 for i in range(1, len(signs)))
        if is_oscillating:
            evidence = TrendEvidence(
                report_dates=report_dates,
                values=values,
                rule_triggered="OSCILLATING_TRAJECTORY",
                explanation="Fluctuating values observed across multiple report dates.",
            )
            return "oscillation", confidence, pct_change, abs_change, evidence

    # Rule 5: Increasing (> +5% overall change)
    if pct_change > 5.0:
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="CONSECUTIVE_INCREASE",
            explanation=f"Parameter value increased by {pct_change}% from baseline.",
        )
        return "increasing", confidence, pct_change, abs_change, evidence

    # Rule 6: Decreasing (< -5% overall change)
    if pct_change < -5.0:
        evidence = TrendEvidence(
            report_dates=report_dates,
            values=values,
            rule_triggered="CONSECUTIVE_DECREASE",
            explanation=f"Parameter value decreased by {abs(pct_change)}% from baseline.",
        )
        return "decreasing", confidence, pct_change, abs_change, evidence

    # Rule 7: Stable (within ±5%)
    evidence = TrendEvidence(
        report_dates=report_dates,
        values=values,
        rule_triggered="STABLE_TRAJECTORY",
        explanation="Parameter reading has remained clinically stable within ±5%.",
    )
    return "stable", confidence, pct_change, abs_change, evidence
