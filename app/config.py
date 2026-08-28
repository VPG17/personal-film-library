from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    tmdb_api_read_access_token: str
    tmdb_base_url: str = "https://api.themoviedb.org/3"
    request_timeout: float = 10.0
    database_url: str = "sqlite:///./filmoteca.db"

@lru_cache
def get_settings() -> Settings:
    return Settings()