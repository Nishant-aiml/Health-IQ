# --------------------------------------------------
# File: system_prompt.py
# Purpose: System prompt builder assembling modular prompt components and context.
# Module: RAG Engine / Prompts
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from backend.app.rag.prompts.instructions import SYSTEM_INSTRUCTIONS
from backend.app.rag.prompts.safety import SAFETY_RULES
from backend.app.rag.prompts.response_format import RESPONSE_FORMAT


class SystemPromptBuilder:
    """
    System Prompt Builder.

    Why it exists:
        Assembles persona instructions, strict anti-hallucination rules, response formatting,
        and full report + guideline context into a cohesive system prompt.
    """

    def build_system_prompt(self, full_context_str: str) -> str:
        parts = [
            SYSTEM_INSTRUCTIONS,
            "\n",
            SAFETY_RULES,
            "\n",
            RESPONSE_FORMAT,
            "\n",
            full_context_str,
        ]
        return "\n".join(parts)


system_prompt_builder = SystemPromptBuilder()
