# --------------------------------------------------
# File: loader.py
# Purpose: Historical data loader sorting and validating multi-report series.
# Module: History Intelligence / Loader
# Used By: History Repository & Services
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List, Dict
from backend.app.history.models import HistoricalParameterReading, ParameterHistorySeries
from backend.app.history.validator import validate_historical_readings


class HistoricalDataLoader:
    """Assembles and validates historical biomarker time series."""

    def build_parameter_series(self, canonical_name: str, raw_readings: List[HistoricalParameterReading]) -> ParameterHistorySeries:
        valid_readings = validate_historical_readings(raw_readings)
        unit = valid_readings[-1].unit if valid_readings else "mg/dL"

        return ParameterHistorySeries(
            canonical_name=canonical_name,
            unit=unit,
            readings=valid_readings,
            available_reports=len(valid_readings),
        )


historical_loader = HistoricalDataLoader()
