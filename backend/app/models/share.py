from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class SharedProfile(SQLModel, table=True):
    __tablename__ = "shared_profiles"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    included_report_ids: str = Field(default="[]", description="JSON array of report IDs included in share")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime
    revoked: bool = Field(default=False)
    share_token: str = Field(unique=True, index=True)
