from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401
from app.database import Base, engine
from app.routers import search


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="Filmoteca personal", lifespan=lifespan)
app.include_router(search.router)