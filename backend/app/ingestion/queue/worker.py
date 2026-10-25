# --------------------------------------------------
# File: worker.py
# Purpose: Background worker pool consumer loop.
# Module: Ingestion Engine / Queue
# Used By: Application Lifespan Hooks
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

import asyncio
from backend.app.ingestion.queue.manager import queue_manager
from backend.app.ingestion.queue.jobs import process_document_job
from backend.app.core.logging import logger

_worker_task = None


async def _worker_loop():
    """
    Background worker loop continuously pulling jobs off the queue.
    """
    logger.info("Ingestion Worker Loop started.")
    while True:
        try:
            job_data = await queue_manager.get_next_job()
            job_id = job_data["job_id"]
            file_bytes = job_data["file_bytes"]
            filename = job_data["filename"]

            await process_document_job(job_id, file_bytes, filename)
            queue_manager.task_done()
        except asyncio.CancelledError:
            logger.info("Ingestion Worker Loop cancelled.")
            break
        except Exception as exc:
            logger.error(f"Unhandled worker error: {exc}")


def start_worker():
    """Starts the background ingestion worker loop."""
    global _worker_task
    if _worker_task is None or _worker_task.done():
        _worker_task = asyncio.create_task(_worker_loop())
        logger.info("Async Ingestion Worker background task created.")


def stop_worker():
    """Stops the background ingestion worker loop."""
    global _worker_task
    if _worker_task and not _worker_task.done():
        _worker_task.cancel()
        logger.info("Async Ingestion Worker background task cancellation requested.")
