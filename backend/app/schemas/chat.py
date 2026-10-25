from typing import List, Optional
from pydantic import BaseModel, Field


class ChatMessageRequest(BaseModel):
    message: str = Field(min_length=1)
    report_id: Optional[int] = None
    prescription_id: Optional[int] = None


class CitationSource(BaseModel):
    source_name: str
    source_url: Optional[str] = None
    chunk_text: str


class ChatMessageResponse(BaseModel):
    session_id: int
    role: str
    content: str
    citations: List[CitationSource] = Field(default_factory=list)
