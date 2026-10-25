# --------------------------------------------------
# File: test_change_analysis.py
# Purpose: Unit tests for Clinical Change Engine deltas and comparison modes.
# Module: Backend Test Suite / Clinical Change
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from datetime import datetime
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.change.analyzer import change_analyzer
from backend.app.history.change.models import ComparisonMode


def test_clinical_change_comparison():
    now = datetime.now()
    t_reading = HistoricalParameterReading(report_id=2, collection_date=now, raw_name="Hb", canonical_name="Hemoglobin", value=14.2, unit="g/dL", severity="NORMAL")
    r_reading = HistoricalParameterReading(report_id=1, collection_date=now, raw_name="Hb", canonical_name="Hemoglobin", value=11.5, unit="g/dL", severity="LOW")

    res = change_analyzer.compare_reports(
        mode=ComparisonMode.PREVIOUS,
        target_report_id=2,
        reference_report_id=1,
        target_readings=[t_reading],
        reference_readings=[r_reading],
        target_score=95.0,
        reference_score=75.0,
    )

    assert res.improved_count == 1
    assert res.health_score_delta == 20.0
    assert res.biomarker_changes[0].change_status == "Improved"
