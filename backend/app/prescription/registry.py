# --------------------------------------------------
# File: registry.py
# Purpose: Prescription Extraction Registry.
# Module: Prescription OCR & Parsing
# Used By: Prescription Services
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.prescription.extractor import prescription_extractor, PrescriptionExtractor
from backend.app.prescription.parser import prescription_parser, PrescriptionParser


class PrescriptionRegistry:
    async def extract_prescription(self, file_bytes: bytes, filename: str):
        return await prescription_extractor.extract_prescription(file_bytes, filename)


prescription_registry = PrescriptionRegistry()
