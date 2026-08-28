from pydantic import BaseModel


class MovieOut(BaseModel):
    id: int
    title: str
    overview: str
    vote_average: float
    vote_count: int
    poster_path: str