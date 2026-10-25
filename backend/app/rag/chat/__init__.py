# --------------------------------------------------
# File: __init__.py
# Purpose: Chat package index.
# Module: RAG Engine / Chat
# Used By: Grounded Chat Service
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.chat.models import ChatRequest, ChatResponse
from backend.app.rag.chat.memory import SlidingWindowMemory, chat_memory
from backend.app.rag.chat.engine import GroundedChatEngine, grounded_chat_engine

__all__ = [
    "ChatRequest",
    "ChatResponse",
    "SlidingWindowMemory",
    "chat_memory",
    "GroundedChatEngine",
    "grounded_chat_engine",
]
