# --------------------------------------------------
# File: __init__.py
# Purpose: Translation Engine package index.
# Module: Translation Engine
# Used By: Services & Application
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from backend.app.i18n.language import SUPPORTED_LANGUAGES, LanguageInfo
from backend.app.i18n.translator import MultilingualTranslator, multilingual_translator, TranslationResult
from backend.app.i18n.registry import TranslationRegistry, translation_registry

__all__ = [
    "SUPPORTED_LANGUAGES",
    "LanguageInfo",
    "MultilingualTranslator",
    "multilingual_translator",
    "TranslationResult",
    "TranslationRegistry",
    "translation_registry",
]
