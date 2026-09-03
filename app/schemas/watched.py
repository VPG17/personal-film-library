from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class WatchedCreate(BaseModel):
    tmdb_id: int
    rate: int = Field(ge=1, le=10)
    comment: str | None = Field(default=None, max_length=500)


class WatchedOut(BaseModel):
    id: UUID
    tmdb_id: int
    rate: int
    comment: str | None
    watched_at: datetime

    model_config = ConfigDict(from_attributes=True)