# --------------------------------------------------
# File: engine.py
# Purpose: Grounded Chat Engine orchestrating Security Validation, Hybrid Retrieval, Context Building, LLM Completion, and Citation Generation.
# Module: RAG Engine / Chat
# Used By: Grounded Chat Service
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import uuid
from typing import Dict, Any
from backend.app.rag.security import security_filter
from backend.app.rag.retrieval import hybrid_retriever
from backend.app.rag.context import context_builder
from backend.app.rag.prompts import system_prompt_builder
from backend.app.rag.providers import grounded_llm_provider
from backend.app.rag.citations import citation_generator
from backend.app.rag.chat.models import ChatResponse
from backend.app.rag.chat.memory import chat_memory
from backend.app.core.logging import logger


class GroundedChatEngine:
    """
    Grounded Chat Engine Orchestrator.

    Why it exists:
        Orchestrates end-to-end grounded report chat:
        1. Validates query against prompt injection filter.
        2. Executes Hybrid Retrieval (FAISS Dense + BM25 Sparse + RRF).
        3. Builds full structured prompt context.
        4. Calls Grounded LLM Provider.
        5. Generates explicit WHO/CDC/NIH/ICMR citations.
        6. Updates multi-turn conversation memory.
    """

    async def process_chat_query(
        self,
        question: str,
        report_analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
        conversation_id: str = None,
    ) -> ChatResponse:
        conv_id = conversation_id or f"conv_{uuid.uuid4().hex[:8]}"

        # Step 1: Security Prompt Injection Check
        security_filter.validate_query_safety(question)

        # Step 2: Hybrid Retrieval
        retrieval_res = hybrid_retriever.retrieve(question)
        chunks = retrieval_res.retrieved_chunks

        # Step 3: Context Building
        full_context = context_builder.build_full_context(
            report_analysis=report_analysis,
            recommendation_bundle=recommendation_bundle,
            retrieved_chunks=chunks,
        )

        # Step 4: System Prompt Assembly
        system_prompt = system_prompt_builder.build_system_prompt(full_context)

        # Step 5: Multi-Turn Conversation History
        history = chat_memory.get_history(conv_id)
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(history)
        messages.append({"role": "user", "content": question})

        # Step 6: Call Grounded LLM Provider
        llm_res = await grounded_llm_provider.generate_chat_completion(messages)
        answer_text = llm_res["content"]

        # Step 7: Citation Generation
        citations = citation_generator.generate_citations(
            retrieved_chunks=chunks,
            report_parameters=report_analysis.get("parameters", []),
        )

        # Update Conversation Memory
        chat_memory.add_message(conv_id, "user", question)
        chat_memory.add_message(conv_id, "assistant", answer_text)

        # Extract used patterns and recommendations for response payload
        used_patterns = [p.get("pattern_name") for p in report_analysis.get("detected_patterns", [])]
        used_recs = [r.get("title") for r in recommendation_bundle.get("recommendations", [])]

        chunk_payloads = [
            {
                "chunk_id": c.chunk_id,
                "title": c.title,
                "source": c.source,
                "score": c.score,
                "excerpt": c.text[:120] + "...",
            }
            for c in chunks
        ]

        logger.info(f"Grounded chat response generated for conv_id '{conv_id}' with {len(citations)} citations.")

        return ChatResponse(
            answer=answer_text,
            citations=citations,
            confidence="HIGH",
            retrieved_chunks=chunk_payloads,
            used_patterns=used_patterns,
            used_recommendations=used_recs,
            conversation_id=conv_id,
        )


grounded_chat_engine = GroundedChatEngine()
