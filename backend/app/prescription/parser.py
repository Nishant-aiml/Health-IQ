# --------------------------------------------------
# File: parser.py
# Purpose: Prescription line and tabular OCR text parser.
# Module: Prescription OCR & Parsing / Parser
# Used By: Prescription Extractor
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

import re
from typing import List
from backend.app.prescription.models import RawPrescriptionItem
from backend.app.prescription.normalizer import normalize_prescription_line, normalize_dosage_string
from backend.app.prescription.validators import validate_prescription_item
from backend.app.core.logging import logger


class PrescriptionParser:
    """Parses OCR text stream into structured RawPrescriptionItem records."""

    FREQ_REGEX = r"\b(1-0-1|1-1-1|1-0-0|0-0-1|OD|BD|TDS|QID|HS|SOS|TWICE DAILY|ONCE DAILY|THRICE DAILY)\b"
    FOOD_REGEX = r"\b(AC|PC|BEFORE FOOD|AFTER FOOD|BEFORE MEAL|AFTER MEAL|WITH FOOD)\b"
    DOSAGE_REGEX = r"\b(\d+\s*(?:mg|g|ml|mcg|iu))\b"
    DURATION_REGEX = r"\b(\d+\s*(?:days|weeks|months|day|week|month))\b"

    def parse_text(self, ocr_text: str) -> List[RawPrescriptionItem]:
        lines = ocr_text.splitlines()
        extracted_items: List[RawPrescriptionItem] = []

        for line in lines:
            clean_line = normalize_prescription_line(line)
            if not clean_line or len(clean_line) < 3:
                continue

            # Look for prescription patterns (Tab. / Cap. / Syr. or frequency codes)
            if re.search(r"^(tab|cap|syr|inj|ointment)\.?", clean_line, re.IGNORECASE) or re.search(self.FREQ_REGEX, clean_line, re.IGNORECASE):
                # Extract dosage
                dosage_match = re.search(self.DOSAGE_REGEX, clean_line, re.IGNORECASE)
                dosage = normalize_dosage_string(dosage_match.group(1)) if dosage_match else "As prescribed"

                # Extract frequency
                freq_match = re.search(self.FREQ_REGEX, clean_line, re.IGNORECASE)
                freq = freq_match.group(1).upper() if freq_match else "OD"

                # Extract food instruction
                food_match = re.search(self.FOOD_REGEX, clean_line, re.IGNORECASE)
                food = food_match.group(1).upper() if food_match else "PC"

                # Extract duration
                duration_match = re.search(self.DURATION_REGEX, clean_line, re.IGNORECASE)
                duration = duration_match.group(1).lower() if duration_match else "7 days"

                # Extract medicine name (strip prefixes, dosage, frequency, food, duration)
                med_name = clean_line
                if dosage_match:
                    med_name = med_name.replace(dosage_match.group(0), "")
                if freq_match:
                    med_name = med_name.replace(freq_match.group(0), "")
                if food_match:
                    med_name = med_name.replace(food_match.group(0), "")
                if duration_match:
                    med_name = med_name.replace(duration_match.group(0), "")

                med_name = re.sub(r"^(tab|cap|syr|inj|ointment)\.?\s*", "", med_name, flags=re.IGNORECASE)
                med_name = re.sub(r"[^\w\s-]", "", med_name).strip()

                if not med_name:
                    continue

                item = RawPrescriptionItem(
                    raw_text=clean_line,
                    medicine_name_raw=med_name,
                    dosage=dosage,
                    frequency_raw=freq,
                    food_instruction_raw=food,
                    duration_raw=duration,
                    ocr_confidence=1.0,
                )

                if validate_prescription_item(item):
                    extracted_items.append(item)

        logger.info(f"PrescriptionParser extracted {len(extracted_items)} medicine item(s) from OCR text.")
        return extracted_items


prescription_parser = PrescriptionParser()
