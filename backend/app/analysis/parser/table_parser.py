# --------------------------------------------------
# File: table_parser.py
# Purpose: Tabular column alignment text parser.
# Module: Analysis Engine / Parser
# Used By: Report Normalizer
# Future Phase: Phase 2A Parsing
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.analysis.parser.line_parser import parse_lab_line


def parse_tabular_blocks(raw_text: str) -> List[Dict[str, Any]]:
    """
    Parses a multi-line document string line by line to extract lab parameters.

    Inputs:
        raw_text: Full document string from OCR extraction.

    Returns:
        List of raw parameter dictionaries.
    """
    parsed_results: List[Dict[str, Any]] = []
    lines = raw_text.splitlines()

    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        parsed_item = parse_lab_line(cleaned_line)
        if parsed_item:
            parsed_results.append(parsed_item)

    return parsed_results
