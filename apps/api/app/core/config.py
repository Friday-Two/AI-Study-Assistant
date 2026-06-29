from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str
    environment: str
    debug: bool

    host: str
    port: int

    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    frontend_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()