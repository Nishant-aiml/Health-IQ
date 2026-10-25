# --------------------------------------------------
# File: models.py
# Purpose: Domain models for tailored exercise, sleep hygiene, hydration, and stress reduction.
# Module: Lifestyle Engine / Models
# Used By: Lifestyle Modules & Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel, Field


class ExercisePlan(BaseModel):
    activity_name: str
    frequency_weekly: str
    duration_minutes_per_session: int
    intensity_level: str = Field(default="Moderate Zone 2 Cardio", description="Light, Moderate Zone 2, Vigorous Zone 3-4")
    physiological_rationale: str
    safety_precautions: str
    evidence_source: str = "WHO Global Guidelines on Physical Activity"


class SleepHygieneItem(BaseModel):
    habit_title: str
    recommendation: str
    circadian_mechanism: str


class SleepHygienePlan(BaseModel):
    target_sleep_duration_hours: str = "7.5 - 8.5 Hours"
    recommended_bedtime_window: str = "10:00 PM - 11:00 PM"
    habits: List[SleepHygieneItem] = Field(default_factory=list)


class StressManagementPlan(BaseModel):
    technique_name: str
    practice_frequency: str
    autonomic_mechanism: str
    recovery_guidance: str


class LifestyleGuidanceBundle(BaseModel):
    report_id: int
    user_id: int
    exercise_plan: List[ExercisePlan] = Field(default_factory=list)
    sleep_hygiene: SleepHygienePlan
    stress_management: StressManagementPlan
    overall_lifestyle_summary: str
