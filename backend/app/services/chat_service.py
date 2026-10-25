# --------------------------------------------------
# File: chat_service.py
# Purpose: Service layer orchestrating Grounded RAG Report Chat.
# Module: RAG Services
# Used By: Chat API Controller
# --------------------------------------------------

from typing import Optional
from sqlmodel import Session
from backend.app.services.report_service import report_service
from backend.app.services.recommendation_service import recommendation_service
from backend.app.rag.chat import grounded_chat_engine, ChatResponse


class ChatService:
    """
    Chat Service.

    Why it exists:
        Consumes Phase 2B report analysis and Phase 2C recommendation bundle
        and calls GroundedChatEngine to answer user questions in selected language.
    """

    async def answer_report_question(
        self,
        session: Session,
        report_id: int,
        question: str,
        conversation_id: str = None,
        language: str = "en",
    ) -> ChatResponse:
        # Step 1: Consume Phase 2B report analysis
        report_analysis = report_service.get_report_analysis(session, report_id)

        # Step 2: Consume Phase 2C recommendation bundle
        recommendation_bundle = recommendation_service.get_recommendations_for_report(session, report_id).dict()

        # Step 3: Process Grounded Chat Query
        response = await grounded_chat_engine.process_chat_query(
            question=question,
            report_analysis=report_analysis,
            recommendation_bundle=recommendation_bundle,
            conversation_id=conversation_id,
        )
        response.language = language
        return response


chat_service = ChatService()
