# --------------------------------------------------
# File: eli10.py
# Purpose: Explain Like I'm 10 (ELI10) plain language analogies for longitudinal health trends.
# Module: Longitudinal Summary Generator / ELI10
# Used By: Summary Generator
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

def generate_trend_eli10(canonical_name: str, direction: str, pct_change: float) -> str:
    """Generates plain language analogies for biomarker trends without diagnosing."""
    key = canonical_name.lower()

    if direction == "recovery":
        return f"Great news! Your {canonical_name} has returned into the safe green zone, just like a battery getting fully recharged."
    elif direction == "persistent_abnormality":
        return f"Your {canonical_name} has stayed outside the recommended range across your last few tests. It's like a tire that needs air pressure checked by your doctor."
    elif direction == "increasing" and "glucose" in key:
        return f"Your blood sugar has drifted upwards by {pct_change}%. Think of it as a river rising slightly after rainfall."
    elif direction == "decreasing" and "cholesterol" in key:
        return f"Your cholesterol has dropped by {abs(pct_change)}%, which means your blood pipes are staying cleaner and smoother."
    elif direction == "stable":
        return f"Your {canonical_name} has stayed steady and balanced, like a sailboat cruising smoothly on calm water."

    return f"Your {canonical_name} changed by {pct_change}% compared to your earlier reports."
