# --------------------------------------------------
# File: simplifier.py
# Purpose: Medical terminology simplifier converting jargon into plain-language analogies for low literacy / senior users.
# Module: Accessibility Engine / Simplifier
# Used By: Accessibility Service Layer
# Future Phase: Phase 3D Multilingual & Voice AI
# --------------------------------------------------

import re
from typing import Dict, Any
from backend.app.accessibility.models import AccessibilityProfileType, AccessibilitySettings


class MedicalTermSimplifier:
    """Simplifies complex medical terms based on chosen Accessibility Profile."""

    SIMPLIFIED_GLOSSARY: Dict[str, str] = {
        "glycemic excursion": "blood sugar jump after eating",
        "glucose excursion": "blood sugar jump after eating",
        "endothelial nitric oxide": "substance that relaxes your blood pipes",
        "hyperkalemia": "high potassium in your blood",
        "bioavailability": "how much medicine your body absorbs",
        "postprandial": "after meal",
        "hepatic glycogen": "sugar stored in your liver",
    }

    def simplify_text(self, text: str, profile_type: AccessibilityProfileType) -> str:
        if profile_type in [AccessibilityProfileType.STANDARD, AccessibilityProfileType.LOW_VISION]:
            return text

        simplified = text
        for jargon, plain in self.SIMPLIFIED_GLOSSARY.items():
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(simplified):
                simplified = pattern.sub(f"{plain} ({jargon})", simplified)

        return simplified


medical_term_simplifier = MedicalTermSimplifier()
