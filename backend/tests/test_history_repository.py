# --------------------------------------------------
# File: test_history_repository.py
# Purpose: Unit tests for historical repository data loader, duplicate dates, out-of-order dates.
# Module: Backend Test Suite / History Repository
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from datetime import datetime, timedelta
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.validator import validate_historical_readings


def test_chronological_sorting_and_deduplication():
    now = datetime.now()
    d1 = now - timedelta(days=30)
    d2 = now - timedelta(days=60)

    # Input out of order with a duplicate
    readings = [
        HistoricalParameterReading(report_id=1, collection_date=now, raw_name="Hb", canonical_name="Hemoglobin", value=13.5, unit="g/dL"),
        HistoricalParameterReading(report_id=2, collection_date=d2, raw_name="Hemoglobin", canonical_name="Hemoglobin", value=14.0, unit="g/dL"),
        HistoricalParameterReading(report_id=3, collection_date=d1, raw_name="HGB", canonical_name="Hemoglobin", value=13.8, unit="g/dL"),
        HistoricalParameterReading(report_id=1, collection_date=now, raw_name="Hb", canonical_name="Hemoglobin", value=13.5, unit="g/dL"), # Duplicate
    ]

    valid = validate_historical_readings(readings)

    assert len(valid) == 3
    # Verify sorted ascending
    assert valid[0].collection_date == d2
    assert valid[1].collection_date == d1
    assert valid[2].collection_date == now
