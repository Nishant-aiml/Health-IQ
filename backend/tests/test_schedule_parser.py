# --------------------------------------------------
# File: test_schedule_parser.py
# Purpose: Unit tests for prescription schedule parser.
# Module: Backend Test Suite / Schedule Interpreter
# Used By: Pytest Execution
# Future Phase: Phase 3A Validation
# --------------------------------------------------

from backend.app.medicine.schedule.parser import schedule_parser


def test_schedule_abbreviation_parsing():
    bd_sched = schedule_parser.parse_schedule("BD", raw_food="after food")
    assert bd_sched.frequency_code == "BD"
    assert bd_sched.times_per_day == 2
    assert bd_sched.relation_to_food == "after_food"
    active_slots = [slot.slot_name for slot in bd_sched.timing_slots if slot.is_active]
    assert "Morning" in active_slots
    assert "Night / Bedtime" in active_slots


def test_numerical_pattern_schedule_parsing():
    tds_sched = schedule_parser.parse_schedule("1-1-1", raw_food="before meals")
    assert tds_sched.frequency_code == "TDS"
    assert tds_sched.times_per_day == 3
    assert tds_sched.relation_to_food == "before_food"
