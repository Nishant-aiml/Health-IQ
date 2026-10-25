# --------------------------------------------------
# File: line_parser.py
# Purpose: Key-value text line parser using regular expressions.
# Module: Analysis Engine / Parser
# Used By: Report Normalizer
# Future Phase: Phase 2A Parsing
# --------------------------------------------------

import re
from typing import Optional, Dict, Any


def parse_lab_line(line_text: str) -> Optional[Dict[str, Any]]:
    """
    Parses a single text line containing a lab parameter name, numerical value, and unit.

    Why it exists:
        Lab reports often format parameters as key-value lines
        (e.g., "Hemoglobin: 11.2 g/dL" or "Fasting Glucose ... 142 mg/dL").

    Inputs:
        line_text: Raw line string extracted by OCR.

    Returns:
        Dict with `raw_name`, `raw_value`, `raw_unit` if matched, else None.
    """
    # Regex pattern matching: Parameter Name : Value Unit
    pattern = r"([A-Za-z0-9\s\(\)\-\_]+)[:\s\.]+(\d+\.?\d*)\s*([A-Za-z\/\%\^\d]+)"
    match = re.search(pattern, line_text)
    
    if match:
        raw_name = match.group(1).strip()
        raw_val_str = match.group(2).strip()
        raw_unit = match.group(3).strip()
        
        try:
            val_float = float(raw_val_str)
            return {
                "raw_name": raw_name,
                "raw_value": val_float,
                "raw_unit": raw_unit,
            }
        except ValueError:
            return None

    return None
