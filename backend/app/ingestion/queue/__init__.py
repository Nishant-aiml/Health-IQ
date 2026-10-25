# --------------------------------------------------
# File: __init__.py
# Purpose: Queue package index.
# Module: Ingestion Engine / Queue
# Used By: Application Lifespan & Document Service
# Future Phase: Phase 2A
# --------------------------------------------------

from backend.app.ingestion.queue.states import JobStage, JobStatus
from backend.app.ingestion.queue.manager import QueueManager, queue_manager
from backend.app.ingestion.queue.jobs import process_document_job
from backend.app.ingestion.queue.worker import start_worker, stop_worker

__all__ = [
    "JobStage",
    "JobStatus",
    "QueueManager",
    "queue_manager",
    "process_document_job",
    "start_worker",
    "stop_worker",
]
