# --------------------------------------------------
# File: manager.py
# Purpose: Asynchronous Queue Manager submitting ingestion jobs to background workers.
# Module: Ingestion Engine / Queue
# Used By: Document Service & API Controllers
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

import asyncio
from typing import Dict, Any
from backend.app.core.logging import logger


class QueueManager:
    """
    Asynchronous Queue Manager.

    Why it exists:
        Manages an in-process `asyncio.Queue` for submitting batch document jobs.
        Ensures HTTP upload endpoints return immediately to the frontend while
        background workers process OCR and parsing asynchronously.
    """

    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()

    async def submit_job(self, job_id: int, file_bytes: bytes, filename: str) -> None:
        """
        Enqueues a job for background execution.

        Inputs:
            job_id: Database ID of the created Job entity.
            file_bytes: Content of file.
            filename: Name of file.
        """
        payload = {
            "job_id": job_id,
            "file_bytes": file_bytes,
            "filename": filename,
        }
        await self._queue.put(payload)
        logger.info(f"Enqueued Job #{job_id} for file '{filename}'. Current queue size: {self._queue.qsize()}")

    async def get_next_job(self) -> Dict[str, Any]:
        """Dequeues the next job payload."""
        return await self._queue.get()

    def task_done(self) -> None:
        """Signals completion of a queued job."""
        self._queue.task_done()

    @property
    def queue_size(self) -> int:
        return self._queue.qsize()


queue_manager = QueueManager()
