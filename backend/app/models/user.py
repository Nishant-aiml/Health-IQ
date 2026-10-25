from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: Optional[str] = Field(default=None, index=True, unique=True)
    password_hash: Optional[str] = Field(default=None)
    name: str = Field(index=True)
    age: int = Field(default=30)
    gender: str = Field(default="other", description="male, female, or other")
    pregnant: bool = Field(default=False)
    preferred_language: str = Field(default="en")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
