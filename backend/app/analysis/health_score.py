# --------------------------------------------------
# File: health_score.py
# Purpose: Calculates an explainable, transparent overall Health Score (0-100).
# Module: Analysis Engine
# Used By: Worker Queue Jobs & Reports API Service
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.analysis.config import SEVERITY_PENALTIES
from backend.app.core.logging import logger


def calculate_health_score(extracted_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculates an explainable 0–100 Health Score based on parameter severity ratio.

    Why it exists:
        Provides a transparent, weighted health summary score grounded in proportion of in-range vs.
        abnormal parameters.
    """
    if not extracted_items:
        return {
            "score": 100,
            "penalties_breakdown": [],
            "total_penalty": 0,
            "summary": "No laboratory parameters provided for scoring.",
        }

    # Filter out metadata lines (Age, Gender, Weight, Height, BMI) from scoring
    excluded_names = {"age", "gender", "weight", "height", "bmi", "suite", "patient id", "sample id"}
    valid_items = [
        item for item in extracted_items
        if item.get("canonical_name", "").strip().lower() not in excluded_names
    ]
    if not valid_items:
        valid_items = extracted_items

    total_penalty_points = 0
    penalties_breakdown: List[Dict[str, Any]] = []

    for item in valid_items:
        c_name = item.get("canonical_name", "Unknown Parameter")
        severity = str(item.get("severity", "normal")).lower()
        is_critical = item.get("is_critical", False)

        if is_critical:
            penalty_points = SEVERITY_PENALTIES["critical"]
        else:
            penalty_points = SEVERITY_PENALTIES.get(severity, 0)

        if penalty_points > 0:
            total_penalty_points += penalty_points
            penalties_breakdown.append({
                "parameter_name": c_name,
                "severity": "critical" if is_critical else severity,
                "points_deducted": penalty_points,
            })

    # Normalized score calculation: average penalty per biomarker normalized against max penalty (35)
    max_possible_penalty_sum = len(valid_items) * 35.0
    penalty_ratio = (total_penalty_points / max_possible_penalty_sum) if max_possible_penalty_sum > 0 else 0.0
    
    # Scale score: 100 - (penalty_ratio * 70)
    final_score = int(round(max(0, min(100, 100 - (penalty_ratio * 75)))))

    if final_score >= 88:
        summary_text = "Optimal overall laboratory health indicators. Biomarkers are well within healthy reference limits."
    elif final_score >= 72:
        summary_text = "Good overall health status with mild parameter deviations requiring dietary or lifestyle guidance."
    elif final_score >= 55:
        summary_text = "Moderate parameter deviations detected. Lifestyle adjustments and follow-up lab tests recommended."
    else:
        summary_text = "Significant abnormal parameter deviations detected. Medical consultation with your physician is advised."

    return {
        "score": final_score,
        "penalties_breakdown": penalties_breakdown,
        "total_penalty": total_penalty_points,
        "summary": summary_text,
    }
