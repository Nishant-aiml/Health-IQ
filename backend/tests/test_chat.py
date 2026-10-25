# --------------------------------------------------
# File: test_chat.py
# Purpose: Integration tests for GroundedChatEngine & multi-turn sliding window memory.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

import asyncio
from backend.app.rag.chat import grounded_chat_engine


def test_grounded_chat_query_processing():
    rep_analysis = {
        "report_id": 1,
        "source_filename": "lab.pdf",
        "health_score": 82,
        "summary": "Mild anemia detected.",
        "parameters": [{"canonical_name": "Hemoglobin", "value": 11.0, "unit": "g/dL", "severity": "moderate"}],
        "detected_patterns": [{"pattern_name": "Nutritional Anemia Pattern", "summary": "Low Hb"}],
    }
    rec_bundle = {"recommendations": [{"title": "Iron Dietary Supplementation", "priority": "HIGH"}]}

    chat_res = asyncio.run(
        grounded_chat_engine.process_chat_query(
            question="Why is my hemoglobin low?",
            report_analysis=rep_analysis,
            recommendation_bundle=rec_bundle,
        )
    )

    assert chat_res.answer != ""
    assert len(chat_res.citations) >= 1
    assert chat_res.conversation_id.startswith("conv_")
