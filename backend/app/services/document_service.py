# --------------------------------------------------
# File: document_service.py
# Purpose: Service orchestrator for document upload, job registration, and batch status polling.
# Module: Document Services
# Used By: Documents API Endpoint Controller
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

import uuid
from typing import List, Dict, Any, Tuple
from sqlmodel import Session
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.models.job import Job
from backend.app.repositories.user_repository import user_repository
from backend.app.repositories.report_repository import report_repository
from backend.app.repositories.job_repository import job_repository
from backend.app.ingestion.queue import queue_manager, JobStage, JobStatus
from backend.app.utils.file_utils import is_supported_document_type
from backend.app.core.exceptions import ValidationException
from backend.app.core.logging import logger


class DocumentService:
    """
    Document Service Orchestrator.

    Why it exists:
        Validates uploaded files, registers default patient profiles, creates `Report` and `Job`
        database rows, enqueues tasks to the background queue, and handles batch polling requests.
    """

    async def submit_document_batch(
        self, session: Session, files: List[Tuple[str, bytes]], doc_type: str = "lab_report"
    ) -> Dict[str, Any]:
        """
        Submits a single or batch upload of document files.

        Inputs:
            session: Active DB session.
            files: List of tuples `(filename, file_bytes)`.
            doc_type: "lab_report" or "prescription".

        Returns:
            Dict containing `batch_id`, `job_ids`, and confirmation message.
        """
        if not files:
            raise ValidationException("At least one document file must be uploaded.")

        # Ensure default user profile exists
        default_user = user_repository.get_by_name(session, "Demo Patient")
        if not default_user:
            default_user = User(name="Demo Patient", age=35, gender="male", pregnant=False, preferred_language="en")
            session.add(default_user)
            session.commit()
            session.refresh(default_user)

        batch_id = str(uuid.uuid4())
        created_job_ids: List[int] = []

        for filename, file_bytes in files:
            if not is_supported_document_type(filename):
                raise ValidationException(f"Unsupported file format for '{filename}'. Allowed: PDF, PNG, JPG, JPEG, DOCX, TXT.")

            # Create Report entity
            report = Report(
                user_id=default_user.id,
                doc_type=doc_type,
                source_filename=filename,
                status=JobStage.QUEUED,
            )
            session.add(report)
            session.commit()
            session.refresh(report)

            # Create Job entity
            job = Job(
                report_id=report.id,
                stage=JobStage.QUEUED,
                status=JobStatus.PENDING,
            )
            session.add(job)
            session.commit()
            session.refresh(job)

            created_job_ids.append(job.id)

            # Enqueue task for background worker
            await queue_manager.submit_job(job.id, file_bytes, filename)

        return {
            "batch_id": batch_id,
            "job_ids": created_job_ids,
            "message": f"Successfully enqueued {len(created_job_ids)} document job(s) for processing.",
        }

    def get_batch_status(self, session: Session, batch_id: str, job_ids: List[int]) -> List[Dict[str, Any]]:
        """
        Returns real-time status for a list of job IDs in a batch.

        Inputs:
            session: Active DB session.
            batch_id: Batch identifier.
            job_ids: List of job database IDs.

        Returns:
            List of status objects per job.
        """
        status_list: List[Dict[str, Any]] = []

        for j_id in job_ids:
            job = job_repository.get_by_id(session, j_id)
            if not job:
                continue
            report = report_repository.get_by_id(session, job.report_id)

            status_list.append({
                "job_id": job.id,
                "report_id": job.report_id,
                "filename": report.source_filename if report else "Unknown",
                "stage": job.stage,
                "status": job.status,
                "error_reason": job.error_reason,
            })

        return status_list


document_service = DocumentService()
