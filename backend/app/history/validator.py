# --------------------------------------------------
# File: validator.py
# Purpose: Data integrity and chronological sanity validation for historical report items.
# Module: History Intelligence / Validator
# Used By: History Repository & Loader
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import List
from backend.app.history.models import HistoricalParameterReading


def validate_historical_readings(readings: List[HistoricalParameterReading]) -> List[HistoricalParameterReading]:
    """Sorts readings chronologically and removes duplicate report date entries."""
    if not readings:
        return []

    # Sort chronologically ascending
    sorted_readings = sorted(readings, key=lambda r: r.collection_date)

    # Deduplicate entries with identical collection date and canonical name
    seen = set()
    deduped = []
    for r in sorted_readings:
        key = (r.canonical_name, r.collection_date.isoformat())
        if key not in seen:
            seen.add(key)
            deduped.append(r)

    return deduped
