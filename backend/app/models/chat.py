from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class ChatSession(SQLModel, table=True):
    __tablename__ = "chat_sessions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    report_id: Optional[int] = Field(default=None, foreign_key="reports.id", index=True)
    prescription_id: Optional[int] = Field(default=None, foreign_key="prescriptions.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ChatMessage(SQLModel, table=True):
    __tablename__ = "chat_messages"

    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="chat_sessions.id", index=True)
    role: str = Field(description="user or assistant")
    content: str
    retrieved_sources: Optional[str] = Field(default="[]", description="JSON array of retrieved source citations")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
