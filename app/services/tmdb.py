from app.config import get_settings
import httpx

settings = get_settings()

async def tmdb_buscador(
    query: str
) -> list[dict]:
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{settings.tmdb_base_url}/search/movie",
            params={"query": query, "language": "es-ES"},
            headers={"Authorization":f"Bearer {settings.tmdb_api_read_access_token}"},
            timeout=settings.request_timeout,
        )
    resp.raise_for_status()
    return resp.json()["results"]