# --------------------------------------------------
# File: parser.py
# Purpose: Prescription code parser (OD, BD, TDS, QID, HS, SOS, AC, PC, 1-0-1).
# Module: Medicine Schedule Interpreter / Parser
# Used By: Medicine Service & Prescription Extractor
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

import re
from typing import List
from backend.app.medicine.schedule.models import NormalizedSchedule, TimeSlot


class ScheduleParser:
    """Parses medical prescription timing abbreviations into data-driven TimeSlot objects."""

    def parse_schedule(self, raw_frequency: str, raw_food: str = "", duration: str = "7 days") -> NormalizedSchedule:
        freq_upper = raw_frequency.upper().strip()
        food_lower = raw_food.lower().strip()

        # Determine relation to food
        relation = "after_food"
        food_instruction = "After meals"

        if "before" in food_lower or "ac" in food_lower:
            relation = "before_food"
            food_instruction = "30 mins Before meals"
        elif "with" in food_lower:
            relation = "with_food"
            food_instruction = "With meals"

        # Build base time slots
        morning = TimeSlot(slot_id="morning", slot_name="Morning", target_time="08:00 AM", is_active=False)
        afternoon = TimeSlot(slot_id="afternoon", slot_name="Afternoon", target_time="01:00 PM", is_active=False)
        evening = TimeSlot(slot_id="evening", slot_name="Evening", target_time="06:00 PM", is_active=False)
        night = TimeSlot(slot_id="night", slot_name="Night / Bedtime", target_time="09:30 PM", is_active=False)

        times_per_day = 1
        freq_code = "OD"
        desc = "Take once daily"

        # Pattern 1: Numerical notation (1-0-1, 1-1-1, 1-0-0, 0-0-1)
        if re.search(r"\b1-0-1\b", freq_upper):
            morning.is_active = True
            night.is_active = True
            times_per_day = 2
            freq_code = "BD"
            desc = f"Take 1 tablet twice daily ({food_instruction}) — Morning & Night"
        elif re.search(r"\b1-1-1\b", freq_upper):
            morning.is_active = True
            afternoon.is_active = True
            night.is_active = True
            times_per_day = 3
            freq_code = "TDS"
            desc = f"Take 1 tablet 3 times daily ({food_instruction}) — Morning, Afternoon & Night"
        elif re.search(r"\b1-0-0\b", freq_upper):
            morning.is_active = True
            times_per_day = 1
            freq_code = "OD"
            desc = f"Take 1 tablet once daily in the Morning ({food_instruction})"
        elif re.search(r"\b0-0-1\b", freq_upper):
            night.is_active = True
            times_per_day = 1
            freq_code = "HS"
            desc = f"Take 1 tablet once daily at Night ({food_instruction})"

        # Pattern 2: Abbreviations (BD, TDS, QID, HS, SOS, OD)
        elif "BD" in freq_upper or "TWICE" in freq_upper:
            morning.is_active = True
            night.is_active = True
            times_per_day = 2
            freq_code = "BD"
            desc = f"Take twice daily ({food_instruction}) — Morning & Night"
        elif "TDS" in freq_upper or "THRICE" in freq_upper or "THREE TIMES" in freq_upper:
            morning.is_active = True
            afternoon.is_active = True
            night.is_active = True
            times_per_day = 3
            freq_code = "TDS"
            desc = f"Take 3 times daily ({food_instruction}) — Morning, Afternoon & Night"
        elif "QID" in freq_upper or "FOUR TIMES" in freq_upper:
            morning.is_active = True
            afternoon.is_active = True
            evening.is_active = True
            night.is_active = True
            times_per_day = 4
            freq_code = "QID"
            desc = f"Take 4 times daily ({food_instruction}) — Morning, Afternoon, Evening & Night"
        elif "HS" in freq_upper or "NIGHT" in freq_upper or "BEDTIME" in freq_upper:
            night.is_active = True
            times_per_day = 1
            freq_code = "HS"
            desc = f"Take once daily at Night / Bedtime ({food_instruction})"
        elif "SOS" in freq_upper or "AS NEEDED" in freq_upper:
            times_per_day = 1
            freq_code = "SOS"
            desc = f"Take as needed (SOS) for acute symptoms ({food_instruction})"
        else:
            morning.is_active = True
            times_per_day = 1
            freq_code = "OD"
            desc = f"Take once daily ({food_instruction})"

        return NormalizedSchedule(
            frequency_code=freq_code,
            times_per_day=times_per_day,
            timing_slots=[morning, afternoon, evening, night],
            relation_to_food=relation,
            food_instruction_en=food_instruction,
            human_description=desc,
            duration=duration,
        )


schedule_parser = ScheduleParser()
