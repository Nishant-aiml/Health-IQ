# --------------------------------------------------
# File: documents.py
# Purpose: Document Batch Ingestion and Status Polling API endpoints.
# Module: API Engine / Endpoints
# Used By: Frontend File Dropzone & Progress Checklist
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form, Query
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.document_service import document_service
from backend.app.schemas.base import BaseResponse
from backend.app.schemas.report import ReportUploadResponse, ReportStatusResponse

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/batch", response_model=BaseResponse[ReportUploadResponse], summary="Submit Document Batch Upload")
async def upload_document_batch(
    files: List[UploadFile] = File(...),
    doc_type: str = Form("lab_report"),
    user_id: Optional[int] = Form(1),
    db_session: Session = Depends(get_db_session),
) -> BaseResponse[ReportUploadResponse]:
    """
    Submits one or multiple PDF, Image, DOCX, or TXT documents for non-blocking background processing.
    """
    files_payload = []
    for uploaded_file in files:
        contents = await uploaded_file.read()
        files_payload.append((uploaded_file.filename, contents))

    submission_result = await document_service.submit_document_batch(
        db_session, files_payload, doc_type=doc_type, user_id=user_id or 1
    )

    return BaseResponse(
        success=True,
        data=ReportUploadResponse(
            batch_id=submission_result["batch_id"],
            job_ids=submission_result["job_ids"],
            message=submission_result["message"],
        ),
        message="Batch submission accepted",
    )


@router.get("/batch/{batch_id}/status", response_model=BaseResponse[List[ReportStatusResponse]], summary="Poll Batch Status")
async def get_batch_status(
    batch_id: str,
    job_ids: List[str] = Query(default=[]),
    db_session: Session = Depends(get_db_session),
) -> BaseResponse[List[ReportStatusResponse]]:
    """
    Polls real-time per-file processing stage progress for a batch submission.
    Supports both repeated query params (job_ids=1&job_ids=2) and comma-separated (job_ids=1,2).
    """
    parsed_ids: List[int] = []
    for raw_item in job_ids:
        for piece in str(raw_item).split(","):
            piece = piece.strip()
            if piece.isdigit():
                parsed_ids.append(int(piece))

    status_list = document_service.get_batch_status(db_session, batch_id, parsed_ids)

    response_items = [
        ReportStatusResponse(
            job_id=item.get("job_id"),
            report_id=item["report_id"],
            filename=item.get("filename"),
            status=item["status"],
            stage=item["stage"],
            error_reason=item["error_reason"],
        )
        for item in status_list
    ]

    return BaseResponse(success=True, data=response_items, message="Status updated")
