# --------------------------------------------------
# File: base.py
# Purpose: Abstract base class for all OCR Provider implementations.
# Module: OCR Engine / Providers
# Used By: PyMuPDFProvider, DoclingProvider, SarvamProvider, VisionProvider
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

from abc import ABC, abstractmethod
from backend.app.ocr.models import OCRExtractionResult


class BaseOCRProvider(ABC):
    """
    Abstract Base Class for OCR Engine Providers.

    Why it exists:
        Enforces a strict contract (`extract`) that every OCR tier must implement.
        Allows the Tiered Pipeline to cycle through providers interchangeably.
    """

    def __init__(self, provider_name: str, timeout_seconds: float = 10.0):
        self.provider_name = provider_name
        self.timeout_seconds = timeout_seconds

    @abstractmethod
    async def extract(self, file_bytes: bytes, filename: str) -> OCRExtractionResult:
        """
        Executes OCR extraction on raw file bytes.

        Inputs:
            file_bytes: Content of PDF/image file.
            filename: Original file name.

        Returns:
            OCRExtractionResult containing structured blocks and extracted text.
        """
        pass
