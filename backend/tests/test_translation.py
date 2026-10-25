# --------------------------------------------------
# File: test_translation.py
# Purpose: Unit tests for Multilingual Translator and Medical Dictionary preservation.
# Module: Backend Test Suite / Translation Engine
# Used By: Pytest Execution
# Future Phase: Phase 3D Validation
# --------------------------------------------------

from backend.app.i18n.translator import multilingual_translator
from backend.app.i18n.language import SUPPORTED_LANGUAGES


def test_supported_languages_list():
    assert len(SUPPORTED_LANGUAGES) == 10
    assert "hi" in SUPPORTED_LANGUAGES
    assert "mr" in SUPPORTED_LANGUAGES
    assert "ta" in SUPPORTED_LANGUAGES


def test_translation_with_medical_preservation():
    text = "What foods should I limit based on my lab report and medicines?"
    res = multilingual_translator.translate_text(text, target_language="hi")

    assert res.target_language == "hi"
    assert res.translation_confidence > 0.9
    assert res.medical_terms_preserved is True
    assert len(res.translated_text) > 0
