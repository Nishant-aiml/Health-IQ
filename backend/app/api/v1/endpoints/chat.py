# --------------------------------------------------
# File: chat.py
# Purpose: Grounded Report Chat API Controller.
# Module: API Engine / Endpoints
# Used By: Frontend Interactive Chat Tab
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.app.api.dependencies import get_db_session
from backend.app.services.chat_service import chat_service
from backend.app.schemas.base import BaseResponse
from backend.app.rag.chat.models import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Grounded Chat"])


@router.post("/{report_id}", response_model=BaseResponse[ChatResponse], summary="Ask Grounded Question About Report")
async def chat_about_report(
    report_id: int,
    request: ChatRequest,
    db_session: Session = Depends(get_db_session),
) -> BaseResponse[ChatResponse]:
    """
    Submits a user question grounded in patient report data and WHO/CDC/NIH/ICMR guidelines.

    Inputs:
        report_id: Database report ID.
        request: ChatRequest payload (question, conversation_id).

    Returns:
        BaseResponse containing ChatResponse with grounded answer, citations, confidence, retrieved chunks, and used patterns.
    """
    chat_res = await chat_service.answer_report_question(
        session=db_session,
        report_id=report_id,
        question=request.question,
        conversation_id=request.conversation_id,
    )
    return BaseResponse(success=True, data=chat_res, message="Grounded response generated successfully.")
