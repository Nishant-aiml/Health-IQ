# --------------------------------------------------
# File: sarvam_provider.py
# Purpose: Tier 3 OCR Provider for scanned/photographed reports using Sarvam Vision Doc AI API.
# Module: OCR Engine / Providers
# Used By: TieredOCRPipeline
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

import time
import io
import zipfile
import asyncio
import httpx
from backend.app.ocr.providers.base import BaseOCRProvider
from backend.app.ocr.models import OCRExtractionResult, OCRPage, OCRBlock
from backend.app.core.config import settings
from backend.app.core.logging import logger


class SarvamProvider(BaseOCRProvider):
    """
    Tier 3 OCR Provider: Sarvam Vision Document Intelligence.

    Why it exists:
        Uses Sarvam Vision 3B multimodal model specialized for Indian lab reports and prescriptions.
        Supports 23 languages (22 Indic + English) and handles mixed printed/handwritten content.

    API Specifications:
        Endpoint: POST https://api.sarvam.ai/doc-ai/v1/job/digitise
        Headers: api-subscription-key
        Data: language="en-IN", output_format="md", content_type="mixed", auto_orient="true"
    """

    def __init__(self, timeout_seconds: float = 15.0):
        super().__init__(provider_name="Sarvam Vision Doc AI", timeout_seconds=timeout_seconds)
        self.base_url = "https://api.sarvam.ai/doc-ai/v1"

    async def extract(
        self,
        file_bytes: bytes,
        filename: str,
        language: str = "en-IN",
        content_type: str = "mixed",
        output_format: str = "md",
    ) -> OCRExtractionResult:
        start_time = time.perf_counter()

        # Verify Sarvam API Key
        api_key = getattr(settings, "SARVAM_API_KEY", None)
        if not api_key:
            logger.info("Sarvam API key unconfigured. Escalating to next OCR provider tier.")
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message="SARVAM_API_KEY unconfigured",
            )

        headers = {"api-subscription-key": api_key}

        try:
            async with httpx.AsyncClient(timeout=self.timeout_seconds) as client:
                # Step 1: Submit Digitization Job
                response = await client.post(
                    f"{self.base_url}/job/digitise",
                    headers=headers,
                    files={"file": (filename, file_bytes)},
                    data={
                        "language": language,
                        "output_format": output_format,
                        "content_type": content_type,
                        "auto_orient": "true",
                    },
                )

                if response.status_code != 200:
                    logger.warning(f"Sarvam job creation returned status {response.status_code}: {response.text}")
                    return OCRExtractionResult(
                        success=False,
                        provider_used=self.provider_name,
                        extracted_text="",
                        error_message=f"Sarvam API status {response.status_code}",
                    )

                job_data = response.json()
                job_id = job_data.get("job_id")
                if not job_id:
                    return OCRExtractionResult(
                        success=False,
                        provider_used=self.provider_name,
                        extracted_text="",
                        error_message="No job_id returned by Sarvam Vision API",
                    )

                logger.info(f"Sarvam Vision job created: {job_id}. Polling for completion...")

                # Step 2: Async Polling Status Loop
                terminal_states = {"completed", "partially_completed", "failed", "rejected"}
                poll_start = time.time()

                while time.time() - poll_start < self.timeout_seconds:
                    await asyncio.sleep(1.5)
                    status_res = await client.get(f"{self.base_url}/job/{job_id}/status", headers=headers)
                    if status_res.status_code == 200:
                        status_data = status_res.json()
                        job_status = status_data.get("status", "")
                        logger.info(f"Sarvam Job #{job_id} status: {job_status}")

                        if job_status in terminal_states:
                            if job_status in {"failed", "rejected"}:
                                return OCRExtractionResult(
                                    success=False,
                                    provider_used=self.provider_name,
                                    extracted_text="",
                                    error_message=f"Sarvam Job ended in state: {job_status}",
                                )
                            break

                # Step 3: Get Download URL
                download_res = await client.get(f"{self.base_url}/job/{job_id}/download-url", headers=headers)
                if download_res.status_code != 200:
                    return OCRExtractionResult(
                        success=False,
                        provider_used=self.provider_name,
                        extracted_text="",
                        error_message="Failed to obtain output download URL from Sarvam",
                    )

                download_url = download_res.json().get("url")
                down_headers = download_res.json().get("headers") or {}

                # Step 4: Download processed ZIP output
                output_res = await client.get(download_url, headers=down_headers)
                if output_res.status_code == 200:
                    zip_content = output_res.content
                    extracted_text = self._parse_zip_output(zip_content)

                    duration = round((time.perf_counter() - start_time) * 1000, 2)
                    return OCRExtractionResult(
                        success=True,
                        provider_used=self.provider_name,
                        extracted_text=extracted_text,
                        confidence=0.98,
                        execution_time_ms=duration,
                    )
                else:
                    return OCRExtractionResult(
                        success=False,
                        provider_used=self.provider_name,
                        extracted_text="",
                        error_message="Failed to download zip output content",
                    )

        except Exception as e:
            logger.error(f"Sarvam Vision OCR request failed: {e}")
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message=str(e),
            )

    def _parse_zip_output(self, zip_bytes: bytes) -> str:
        """
        Unzips Sarvam output and extracts text content from markdown/html files.
        """
        text_chunks = []
        try:
            with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
                for filename in z.namelist():
                    if filename.endswith(".md") or filename.endswith(".html") or filename.endswith(".txt"):
                        with z.open(filename) as f:
                            content = f.read().decode("utf-8", errors="ignore")
                            if content.strip():
                                text_chunks.append(content.strip())
            return "\n\n".join(text_chunks) if text_chunks else "No text extracted from Sarvam output archive."
        except Exception as exc:
            logger.error(f"Error parsing Sarvam ZIP output: {exc}")
            return ""
