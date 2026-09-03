# app/models/watched.py
import uuid
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import uuid_pk


class WatchedMovie(Base):
    __tablename__ = "watched_movies"

    id: Mapped[uuid.UUID] = uuid_pk()
    tmdb_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    rate: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str | None] = mapped_column(String(500))
    watched_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    __table_args__ = (UniqueConstraint("tmdb_id", name="uq_watched_tmdb_id"),)