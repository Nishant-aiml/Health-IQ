# --------------------------------------------------
# File: cache.py
# Purpose: Translation memory cache for instant language switching without network latency.
# Module: Translation Engine / Cache
# Used By: Translator
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from typing import Dict, Optional


class TranslationCache:
    """In-memory translation cache storing translated strings per target language."""

    def __init__(self):
        self._cache: Dict[str, Dict[str, str]] = {}

    def get(self, text: str, target_lang: str) -> Optional[str]:
        return self._cache.get(target_lang, {}).get(text)

    def set(self, text: str, target_lang: str, translated: str):
        if target_lang not in self._cache:
            self._cache[target_lang] = {}
        self._cache[target_lang][text] = translated


translation_cache = TranslationCache()
