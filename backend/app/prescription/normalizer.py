# --------------------------------------------------
# File: normalizer.py
# Purpose: Prescription line and dosage text normalizer.
# Module: Prescription OCR & Parsing / Normalizer
# Used By: Prescription Parser
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

import re


def normalize_prescription_line(line: str) -> str:
    """Cleans OCR artifacts and standardizes prescription text lines."""
    line = re.sub(r"\s+", " ", line).strip()
    return line


def normalize_dosage_string(raw_dosage: str) -> str:
    """Normalizes dosage strings (e.g. '500 mg' -> '500mg', '10 mg' -> '10mg')."""
    raw_dosage = raw_dosage.strip()
    raw_dosage = re.sub(r"(\d+)\s+(mg|g|ml|mcg|iu)\b", r"\1\2", raw_dosage, flags=re.IGNORECASE)
    return raw_dosage
