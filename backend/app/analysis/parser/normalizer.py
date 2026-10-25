# --------------------------------------------------
# File: normalizer.py
# Purpose: Orchestrates text parsing and canonical parameter dictionary resolution.
# Module: Analysis Engine / Parser
# Used By: Document Ingestion Worker
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.analysis.parser.table_parser import parse_tabular_blocks
from backend.app.analysis.canonical import (
    resolve_canonical_name,
    normalize_unit,
    is_physiologically_plausible,
)
from backend.app.core.logging import logger


def normalize_report_data(raw_ocr_text: str) -> List[Dict[str, Any]]:
    """
    Parses OCR text and canonicalizes all parameter names, units, and values.

    Why it exists:
        Raw OCR text contains lab-specific terminology ("Hb", "FBS", "S. Creatinine").
        This function canonicalizes them into standard names ("Hemoglobin", "Fasting Blood Sugar")
        and flags unrecognized lines cleanly.

    Inputs:
        raw_ocr_text: Document text output from OCR pipeline.

    Returns:
        List of structured dictionaries containing:
        `{canonical_name, raw_name, value, unit, is_recognized, is_valid}`
    """
    raw_extracted_items = parse_tabular_blocks(raw_ocr_text)
    normalized_list: List[Dict[str, Any]] = []

    for item in raw_extracted_items:
        raw_name = item["raw_name"]
        raw_value = item["raw_value"]
        raw_unit = item["raw_unit"]

        canonical_name = resolve_canonical_name(raw_name)

        if canonical_name:
            norm_val, norm_unit = normalize_unit(canonical_name, raw_value, raw_unit)
            valid = is_physiologically_plausible(canonical_name, norm_val)

            normalized_list.append({
                "canonical_name": canonical_name,
                "raw_name": raw_name,
                "value": norm_val,
                "unit": norm_unit,
                "is_recognized": True,
                "is_valid": valid,
            })
        else:
            logger.info(f"Unrecognized parameter flagged: '{raw_name}' with value {raw_value}")
            normalized_list.append({
                "canonical_name": raw_name,
                "raw_name": raw_name,
                "value": raw_value,
                "unit": raw_unit,
                "is_recognized": False,
                "is_valid": True,
            })

    return normalized_list
