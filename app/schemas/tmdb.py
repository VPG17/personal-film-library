from pydantic import BaseModel, computed_field

class MovieOut(BaseModel):
    id: int
    title: str
    overview: str | None = None
    release_date: str | None = None
    vote_average: float
    vote_count: int
    poster_path: str | None = None

    @computed_field
    @property
    def poster_url(self) -> str | None:
        if not self.poster_path:
            return None
        return f"https://image.tmdb.org/t/p/w342{self.poster_path}"