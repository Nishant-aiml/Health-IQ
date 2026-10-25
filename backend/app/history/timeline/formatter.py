# --------------------------------------------------
# File: formatter.py
# Purpose: Timeline event badge and human-readable date formatting helper.
# Module: Timeline Generator / Formatter
# Used By: Timeline Components & Service
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from datetime import datetime


def format_timeline_date(dt: datetime) -> str:
    """Formats datetime to 'MMM DD, YYYY' string."""
    return dt.strftime("%b %d, %Y")
