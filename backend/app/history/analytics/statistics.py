# --------------------------------------------------
# File: statistics.py
# Purpose: Descriptive time-series statistics engine (mean, median, min, max, std dev, rate of change).
# Module: Time-Series Analytics / Statistics
# Used By: History Service & Trend Analyzer
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

import statistics
from typing import List
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.analytics.models import AnalyticsResult
from backend.app.history.analytics.variability import calculate_variability


class TimeSeriesStatisticsEngine:
    """Computes descriptive time-series statistics without predictive forecasting."""

    def compute_statistics(self, canonical_name: str, readings: List[HistoricalParameterReading]) -> AnalyticsResult:
        if not readings:
            return AnalyticsResult(
                canonical_name=canonical_name,
                unit="mg/dL",
                sample_count=0,
                mean_value=0.0,
                median_value=0.0,
                min_value=0.0,
                max_value=0.0,
                std_dev=0.0,
                rate_of_change_per_month=0.0,
                variability_index=0.0,
                variability_level="LOW",
            )

        values = [r.value for r in readings]
        unit = readings[-1].unit
        sample_count = len(values)

        mean_val = round(float(statistics.mean(values)), 2)
        median_val = round(float(statistics.median(values)), 2)
        min_val = round(float(min(values)), 2)
        max_val = round(float(max(values)), 2)

        std_dev = round(float(statistics.stdev(values)), 2) if sample_count > 1 else 0.0
        cv_percent, var_level = calculate_variability(mean_val, std_dev)

        # Rate of change per 30 days
        rate_of_change = 0.0
        if sample_count > 1:
            first = readings[0]
            last = readings[-1]
            days_diff = (last.collection_date - first.collection_date).days
            val_diff = last.value - first.value
            if days_diff > 0:
                rate_of_change = round((val_diff / days_diff) * 30.0, 2)

        return AnalyticsResult(
            canonical_name=canonical_name,
            unit=unit,
            sample_count=sample_count,
            mean_value=mean_val,
            median_value=median_val,
            min_value=min_val,
            max_value=max_val,
            std_dev=std_dev,
            rate_of_change_per_month=rate_of_change,
            variability_index=cv_percent,
            variability_level=var_level,
        )


time_series_statistics_engine = TimeSeriesStatisticsEngine()
