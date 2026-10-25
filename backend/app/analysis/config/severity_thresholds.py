# --------------------------------------------------
# File: severity_thresholds.py
# Purpose: Configurable parameter deviation severity thresholds.
# Module: Analysis Engine / Config
# Used By: Severity Evaluator
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

from typing import Dict, Any

# Configurable Percentage Deviation Thresholds from Normal Range Midpoint
SEVERITY_THRESHOLDS: Dict[str, Dict[str, float]] = {
    "default": {
        "mild_percent": 15.0,      # 0% - 15% deviation beyond range -> Mild
        "moderate_percent": 35.0,  # 15% - 35% deviation -> Moderate
                                   # > 35% deviation -> Severe
    },
    "Hemoglobin": {
        "mild_drop": 1.0,         # g/dL drop below normal low
        "moderate_drop": 2.5,     # g/dL drop below normal low
    },
    "Fasting Blood Sugar": {
        "mild_mgdl": 125.0,       # 100-125 mg/dL -> Pre-diabetes / Mild
        "moderate_mgdl": 180.0,   # 126-180 mg/dL -> Moderate
                                  # > 180 mg/dL -> Severe
    },
}
