# --------------------------------------------------
# File: memory.py
# Purpose: Sliding window multi-turn conversation memory.
# Module: RAG Engine / Chat
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import Dict, List


class SlidingWindowMemory:
    """
    Sliding Window Conversation Memory.

    Why it exists:
        Stores the last N dialogue turns per session to maintain multi-turn chat continuity.
    """

    def __init__(self, max_turns: int = 5):
        self.max_turns = max_turns
        self._conversations: Dict[str, List[Dict[str, str]]] = {}

    def add_message(self, conversation_id: str, role: str, content: str):
        if conversation_id not in self._conversations:
            self._conversations[conversation_id] = []

        history = self._conversations[conversation_id]
        history.append({"role": role, "content": content})

        # Enforce sliding window capacity
        if len(history) > self.max_turns * 2:
            self._conversations[conversation_id] = history[-self.max_turns * 2 :]

    def get_history(self, conversation_id: str) -> List[Dict[str, str]]:
        return self._conversations.get(conversation_id, [])


chat_memory = SlidingWindowMemory()
