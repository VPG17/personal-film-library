from fastapi import APIRouter, HTTPException
from app.services.tmdb import tmdb_buscador
from app.schemas.tmdb_schema import MovieOut

class TMDBError(Exception):
    """Algo falló hablando con TMDB."""

class TMDBTimeout(TMDBError):
    pass

router = APIRouter(tags=["tmdb"])

@router.get("/search", response_model=list[MovieOut])
async def search(title: str):
    try:
        return await tmdb_buscador(title)
    except TMDBTimeout:
        raise HTTPException(status_code=504, detail= "El catálogo tardó demasiado. Inténtalo de nuevo.")
    except TMDBError:
        raise HTTPException(status_code=502, detail="No se pudo consultar el catálogo de películas.")