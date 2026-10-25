# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for Translation Engine.
# Module: Translation Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from backend.app.i18n.translator import multilingual_translator, MultilingualTranslator


class TranslationRegistry:
    def get_translator(self) -> MultilingualTranslator:
        return multilingual_translator


translation_registry = TranslationRegistry()
