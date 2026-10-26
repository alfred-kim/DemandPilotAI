"""Validated application settings sourced from environment variables."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Foundational settings shared by application modules.

    Environment variables use the ``DEMANDPILOT_`` prefix, for example
    ``DEMANDPILOT_ENVIRONMENT=test``.
    """

    model_config = SettingsConfigDict(
        env_prefix="DEMANDPILOT_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        frozen=True,
    )

    environment: Literal["development", "test", "staging", "production"] = "development"
    log_level: str = "INFO"
    log_format: Literal["text", "json"] = "text"
    data_dir: Path = Path("data")
    database_url: str = "postgresql+psycopg://localhost/demandpilot"
    database_pool_size: int = Field(default=5, ge=1, le=100)
    database_max_overflow: int = Field(default=10, ge=0, le=100)

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
            raise ValueError("log_level must be DEBUG, INFO, WARNING, ERROR, or CRITICAL")
        return normalized

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("database_url must not be empty")
        return value


@lru_cache
def get_settings() -> Settings:
    """Return the process settings, cached so environment is read once."""

    return Settings()
