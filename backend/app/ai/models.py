# --------------------------------------------------
# File: models.py
# Purpose: Strongly typed Pydantic domain models for AI recommendations, evidence, and insights.
# Module: AI Engine
# Used By: Recommendation Engine, Evidence Builder, Doctor Questions, API Controllers
# Future Phase: Phase 2C Recommendation Engine & Phase 2D RAG
# --------------------------------------------------

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class PriorityLevel(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"


class ConfidenceLevel(str, Enum):
    VERY_HIGH = "Very High"
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"


class Recommendation(BaseModel):
    """
    Strongly typed recommendation object.
    """

    recommendation_id: str = Field(..., description="Stable identifier e.g. ANEMIA_LOW_HB")
    title: str
    summary: str
    explanation: str
    severity: str = Field(default="normal")
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM)
    category: str = Field(default="lifestyle", description="dietary, medical_followup, lifestyle, diagnostic")
    supporting_parameters: List[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.HIGH)
    recommendation_type: str = Field(default="rule_based")
    generated_by: str = Field(default="ClinicalRuleEngine")


class Evidence(BaseModel):
    """
    Explicit reasoning chain object explaining why a recommendation was generated.
    """

    parameter_name: str
    observed_value: float
    unit: str
    normal_range: str
    severity: str
    detected_pattern: Optional[str] = None
    reasoning_chain: List[str] = Field(default_factory=list)


class Limitation(BaseModel):
    """
    Mandatory clinical context and informational disclaimer object.
    """

    notice: str
    disclaimer_type: str = Field(default="informational")
    clinical_context_required: bool = True


class DoctorQuestion(BaseModel):
    """
    Intelligent doctor discussion question for medical consultations.
    """

    question_text: str
    target_parameter: str
    clinical_rationale: str
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM)


class HealthInsight(BaseModel):
    """
    High-level clinical summary insight object.
    """

    insight_type: str
    headline: str
    description: str
    importance: PriorityLevel = Field(default=PriorityLevel.MEDIUM)


class RecommendationBundle(BaseModel):
    """
    Complete aggregated response payload returned by Recommendation Service & API.
    """

    report_id: int
    health_score: int
    health_score_summary: str
    detected_patterns: List[Dict[str, Any]] = Field(default_factory=list)
    recommendations: List[Recommendation] = Field(default_factory=list)
    evidence_chains: List[Evidence] = Field(default_factory=list)
    limitations: List[Limitation] = Field(default_factory=list)
    doctor_questions: List[DoctorQuestion] = Field(default_factory=list)
    eli10_explanation: str
