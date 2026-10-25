# --------------------------------------------------
# File: __init__.py
# Purpose: Prompts package index.
# Module: RAG Engine / Prompts
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.prompts.instructions import SYSTEM_INSTRUCTIONS
from backend.app.rag.prompts.safety import SAFETY_RULES
from backend.app.rag.prompts.response_format import RESPONSE_FORMAT
from backend.app.rag.prompts.system_prompt import SystemPromptBuilder, system_prompt_builder

__all__ = [
    "SYSTEM_INSTRUCTIONS",
    "SAFETY_RULES",
    "RESPONSE_FORMAT",
    "SystemPromptBuilder",
    "system_prompt_builder",
]
