# --------------------------------------------------
# File: validators.py
# Purpose: Data validity and sanity check validators for extracted prescription items.
# Module: Prescription OCR & Parsing / Validators
# Used By: Prescription Parser
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.prescription.models import RawPrescriptionItem


def validate_prescription_item(item: RawPrescriptionItem) -> bool:
    """Validates extracted medicine record for mandatory fields."""
    if not item.medicine_name_raw or len(item.medicine_name_raw.strip()) < 2:
        return False
    # Reject header keywords
    invalid_keywords = ["prescription", "doctor", "patient", "signature", "date", "hospital", "clinic", "rx"]
    if item.medicine_name_raw.lower().strip() in invalid_keywords:
        return False
    return True
