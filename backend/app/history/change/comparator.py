# --------------------------------------------------
# File: comparator.py
# Purpose: Compares reports across comparison modes (Current vs Previous, Current vs Baseline, Current vs Best, Custom Range).
# Module: Clinical Change Engine / Comparator
# Used By: Change Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Dict
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.change.models import BiomarkerChangeItem, ComparisonMode


class ClinicalComparator:
    """Evaluates comparative deltas between target and reference biomarker readings."""

    def compare_readings(
        self,
        canonical_name: str,
        target_reading: HistoricalParameterReading,
        reference_reading: HistoricalParameterReading,
    ) -> BiomarkerChangeItem:
        unit = target_reading.unit
        target_val = target_reading.value
        ref_val = reference_reading.value

        abs_diff = round(target_val - ref_val, 2)
        pct_diff = 0.0
        if ref_val != 0:
            pct_diff = round(((target_val - ref_val) / abs(ref_val)) * 100, 1)

        # Determine if change represents Improvement, Unchanged, or Worsening
        target_sev = target_reading.severity
        ref_sev = reference_reading.severity

        change_status = "Unchanged"
        sig = "LOW"

        if ref_sev in ["ELEVATED", "CRITICAL"] and target_sev == "NORMAL":
            change_status = "Improved"
            sig = "HIGH"
        elif ref_sev == "NORMAL" and target_sev in ["ELEVATED", "CRITICAL"]:
            change_status = "Worsened"
            sig = "HIGH"
        elif abs(pct_diff) <= 3.0:
            change_status = "Unchanged"
            sig = "LOW"
        elif target_sev == "NORMAL" and ref_sev == "NORMAL":
            change_status = "Unchanged"
            sig = "LOW"
        elif pct_diff < 0 and "Cholesterol" in canonical_name or "Glucose" in canonical_name or "Triglycerides" in canonical_name:
            change_status = "Improved" if target_val < ref_val else "Worsened"
            sig = "MODERATE"
        elif pct_diff > 0 and "Hemoglobin" in canonical_name and target_val > ref_val:
            change_status = "Improved"
            sig = "MODERATE"
        elif pct_diff < 0:
            change_status = "Improved" if ref_sev == "ELEVATED" else "Worsened"
            sig = "MODERATE"
        else:
            change_status = "Worsened" if ref_sev == "NORMAL" else "Improved"
            sig = "MODERATE"

        note = f"Compared with reference value ({ref_val} {unit}), {canonical_name} changed by {abs_diff} {unit} ({pct_diff}%)."

        return BiomarkerChangeItem(
            canonical_name=canonical_name,
            unit=unit,
            target_value=target_val,
            reference_value=ref_val,
            absolute_change=abs_diff,
            percentage_change=pct_diff,
            change_status=change_status,
            clinical_significance=sig,
            summary_note=note,
        )


clinical_comparator = ClinicalComparator()
