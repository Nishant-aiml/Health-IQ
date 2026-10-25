# --------------------------------------------------
# File: models.py
# Purpose: Data-driven TimeSlot and NormalizedSchedule models for prescription medicine timing.
# Module: Medicine Schedule Interpreter / Models
# Used By: Schedule Parser, Frontend ScheduleTimeline
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from pydantic import BaseModel, Field


class TimeSlot(BaseModel):
    """Data-driven daily time slot model."""

    slot_id: str = Field(..., description="morning, afternoon, evening, night")
    slot_name: str
    target_time: str
    is_active: bool = False
    instruction: str = Field(default="Take with water")


class NormalizedSchedule(BaseModel):
    """Complete parsed daily schedule object."""

    frequency_code: str = Field(..., description="OD, BD, TDS, QID, HS, SOS")
    times_per_day: int = Field(default=1)
    timing_slots: List[TimeSlot] = Field(default_factory=list)
    relation_to_food: str = Field(default="after_food", description="before_food, after_food, with_food")
    food_instruction_en: str = Field(default="After meals")
    human_description: str
    duration: str = Field(default="As prescribed")
