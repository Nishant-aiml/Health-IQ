# --------------------------------------------------
# File: sleep.py
# Purpose: Sleep hygiene principles, circadian light exposure, and restorative sleep guidance.
# Module: Lifestyle Engine / Sleep
# Used By: Lifestyle Service Layer
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from backend.app.lifestyle.models import SleepHygienePlan, SleepHygieneItem


def generate_sleep_hygiene_plan() -> SleepHygienePlan:
    habits = [
        SleepHygieneItem(
            habit_title="Morning Sunlight Exposure",
            recommendation="Get 10-15 minutes of direct outdoor morning sunlight within 1 hour of waking.",
            circadian_mechanism="Sets master suprachiasmatic nucleus (SCN) circadian clock, triggering nocturnal melatonin synthesis 14-16 hours later.",
        ),
        SleepHygieneItem(
            habit_title="Blue Light & Screen Sunset",
            recommendation="Dim room lighting and stop using smartphone/laptop screens 60 minutes before bedtime.",
            circadian_mechanism="Prevents melanopsin retinal ganglion cell stimulation, allowing natural pineal melatonin release.",
        ),
        SleepHygieneItem(
            habit_title="Cool & Dark Bedroom Environment",
            recommendation="Maintain bedroom temperature between 18-21°C (65-70°F) with blackout curtains.",
            circadian_mechanism="Facilitates mandatory 1°C drop in core body temperature required for initiating deep slow-wave sleep.",
        ),
    ]

    return SleepHygienePlan(
        target_sleep_duration_hours="7.5 - 8.5 Hours",
        recommended_bedtime_window="10:00 PM - 11:00 PM",
        habits=habits,
    )
