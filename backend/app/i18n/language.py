# --------------------------------------------------
# File: language.py
# Purpose: Supported regional Indian language definitions and metadata.
# Module: Translation Engine / Languages
# Used By: Translator & Frontend Selector
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from typing import Dict
from pydantic import BaseModel


class LanguageInfo(BaseModel):
    code: str
    name: str
    native_name: str


SUPPORTED_LANGUAGES: Dict[str, LanguageInfo] = {
    "en": LanguageInfo(code="en", name="English", native_name="English"),
    "hi": LanguageInfo(code="hi", name="Hindi", native_name="हिंदी"),
    "mr": LanguageInfo(code="mr", name="Marathi", native_name="मराठी"),
    "ta": LanguageInfo(code="ta", name="Tamil", native_name="தமிழ்"),
    "te": LanguageInfo(code="te", name="Telugu", native_name="తెలుగు"),
    "gu": LanguageInfo(code="gu", name="Gujarati", native_name="ગુજરાતી"),
    "pa": LanguageInfo(code="pa", name="Punjabi", native_name="ਪੰਜਾਬੀ"),
    "bn": LanguageInfo(code="bn", name="Bengali", native_name="বাংলা"),
    "ml": LanguageInfo(code="ml", name="Malayalam", native_name="മലയാളം"),
    "kn": LanguageInfo(code="kn", name="Kannada", native_name="ಕನ್ನಡ"),
}
