# --------------------------------------------------
# File: formatter.py
# Purpose: Human readable schedule formatting helper utilities.
# Module: Medicine Schedule Interpreter / Formatter
# Used By: Medicine Service & Frontend UI Components
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.schedule.models import NormalizedSchedule


def format_schedule_badge(schedule: NormalizedSchedule) -> str:
    """Formats short badge text for medicine cards (e.g. 'BD · Twice Daily · After Food')."""
    return f"{schedule.frequency_code} · {schedule.human_description}"
