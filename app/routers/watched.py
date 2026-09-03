from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.database import DbSession
from app.models.watched import WatchedMovie
from app.schemas.watched import WatchedCreate, WatchedOut


router = APIRouter(prefix="/watched", tags=["watched"])


@router.post("", response_model=WatchedOut, status_code=201)
def create_watched(request: WatchedCreate, db: DbSession):
    film = WatchedMovie(**request.model_dump())
    db.add(film)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Esa película ya está en tu lista.")
    db.refresh(film)
    return(film)

@router.get("", response_model=list[WatchedOut])
def list_watched(db: DbSession):
    return db.execute(
        select(WatchedMovie).order_by(WatchedMovie.watched_at.desc())
    ).scalars().all()