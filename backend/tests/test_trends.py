# --------------------------------------------------
# File: test_trends.py
# Purpose: Unit tests for trend detection rules (Recovery, Persistent Abnormality, Rapid Change, Increasing, Decreasing, Stable).
# Module: Backend Test Suite / Trend Engine
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from datetime import datetime, timedelta
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.trends.analyzer import trend_analyzer


def test_trend_recovery_detection():
    now = datetime.now()
    readings = [
        HistoricalParameterReading(report_id=1, collection_date=now - timedelta(days=60), raw_name="Fasting Glucose", canonical_name="Fasting Blood Sugar", value=145.0, unit="mg/dL", severity="ELEVATED"),
        HistoricalParameterReading(report_id=2, collection_date=now, raw_name="Fasting Glucose", canonical_name="Fasting Blood Sugar", value=95.0, unit="mg/dL", severity="NORMAL"),
    ]

    res = trend_analyzer.analyze_series("Fasting Blood Sugar", readings)
    assert res.direction == "recovery"
    assert res.evidence.rule_triggered == "RECOVERY_TO_NORMAL_RANGE"


def test_trend_persistent_abnormality_detection():
    now = datetime.now()
    readings = [
        HistoricalParameterReading(report_id=1, collection_date=now - timedelta(days=60), raw_name="Total Cholesterol", canonical_name="Total Cholesterol", value=240.0, unit="mg/dL", severity="ELEVATED"),
        HistoricalParameterReading(report_id=2, collection_date=now, raw_name="Total Cholesterol", canonical_name="Total Cholesterol", value=250.0, unit="mg/dL", severity="ELEVATED"),
    ]

    res = trend_analyzer.analyze_series("Total Cholesterol", readings)
    assert res.direction == "persistent_abnormality"
    assert res.evidence.rule_triggered == "PERSISTENT_ABNORMALITY"
