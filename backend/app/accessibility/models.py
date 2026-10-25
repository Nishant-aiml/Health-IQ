# --------------------------------------------------
# File: models.py
# Purpose: Domain models for Accessibility Profiles (Standard, Senior Mode, Low Vision, Cognitive Support).
# Module: Accessibility Engine / Models
# Used By: Simplifier & UI Controller
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

from enum import Enum
from pydantic import BaseModel, Field


class AccessibilityProfileType(str, Enum):
    STANDARD = "Standard"
    SENIOR = "Senior Mode (Large Text & Slow Audio)"
    LOW_VISION = "Low Vision (High Contrast)"
    COGNITIVE_SUPPORT = "Cognitive Support (Ultra-Simplified ELI10)"


class AccessibilitySettings(BaseModel):
    profile_type: AccessibilityProfileType = AccessibilityProfileType.STANDARD
    font_scale: float = Field(default=1.0, description="Multiplier for UI font size: 1.0, 1.25, 1.5")
    speech_rate: float = Field(default=1.0, description="Audio speed rate: 1.0 or 0.85")
    high_contrast: bool = False
    reading_complexity_level: str = "Standard ELI10"
