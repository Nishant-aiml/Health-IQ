# --------------------------------------------------
# File: score_penalties.py
# Purpose: Configurable Health Score point penalties and weighting rules.
# Module: Analysis Engine / Config
# Used By: Health Score Calculator
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

# Health Score Point Deductions per Parameter Severity Level
SEVERITY_PENALTIES = {
    "normal": 0,
    "mild": 5,
    "moderate": 12,
    "severe": 25,
    "critical": 35,
}

# Maximum allowed overall penalty cap to prevent extreme runaway deductions on large reports
MAX_TOTAL_PENALTY = 100
