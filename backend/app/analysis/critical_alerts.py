# --------------------------------------------------
# File: critical_alerts.py
# Purpose: Evaluates dangerous thresholds requiring emergency medical attention.
# Module: Analysis Engine
# Used By: Worker Queue Jobs, Health Score, Frontend Alert Banner
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import List, Dict, Any


# Dangerous Clinical Critical Value Thresholds
CRITICAL_THRESHOLDS = {
    "Fasting Blood Sugar": {"high": 300.0, "reason": "Severe hyperglycemia risk"},
    "Hemoglobin": {"low": 7.0, "reason": "Severe anemia / oxygen delivery risk"},
    "Platelet Count": {"low": 50.0, "reason": "Severe thrombocytopenia / bleeding risk"},
    "Serum Creatinine": {"high": 4.0, "reason": "Acute kidney injury risk"},
    "White Blood Cell Count": {"low": 2.0, "high": 30.0, "reason": "Critical infection / leukopenia risk"},
}


def evaluate_critical_alerts(extracted_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Evaluates extracted parameters against dangerous critical threshold baselines.

    Why it exists:
        Critical medical values require an immediate, distinct emergency alert tier above
        routine high/low flags (e.g. red banner).

    Inputs:
        extracted_items: List of normalized parameter dicts.

    Returns:
        List of structured critical alert objects.
    """
    critical_alerts: List[Dict[str, Any]] = []

    for item in extracted_items:
        c_name = item.get("canonical_name", "")
        value = item.get("value")

        if value is None or c_name not in CRITICAL_THRESHOLDS:
            continue

        rules = CRITICAL_THRESHOLDS[c_name]
        is_alert = False
        alert_reason = rules["reason"]

        if "low" in rules and value < rules["low"]:
            is_alert = True
        elif "high" in rules and value > rules["high"]:
            is_alert = True

        if is_alert:
            critical_alerts.append({
                "is_critical": True,
                "parameter_name": c_name,
                "value": value,
                "unit": item.get("unit", ""),
                "reason": alert_reason,
                "recommended_action": "Seek immediate professional medical evaluation.",
            })

    return critical_alerts
