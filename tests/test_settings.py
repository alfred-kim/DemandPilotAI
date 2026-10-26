"""Tests for configuration defaults and validation."""

import pytest
from pydantic import ValidationError

from demandpilot.settings import Settings


def test_settings_have_safe_development_defaults() -> None:
    settings = Settings()

    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.data_dir.as_posix() == "data"
    assert settings.database_pool_size == 5


@pytest.mark.parametrize("level", ["DEBUG", "warning", "ERROR"])
def test_log_level_is_normalized(level: str) -> None:
    assert Settings(log_level=level).log_level == level.upper()


def test_invalid_log_level_is_rejected() -> None:
    with pytest.raises(ValidationError, match="log_level"):
        Settings(log_level="TRACE")


def test_invalid_environment_is_rejected() -> None:
    with pytest.raises(ValidationError, match="environment"):
        Settings(environment="local")  # type: ignore[arg-type]


@pytest.mark.parametrize("pool_size", [0, 101])
def test_invalid_database_pool_size_is_rejected(pool_size: int) -> None:
    with pytest.raises(ValidationError, match="database_pool_size"):
        Settings(database_pool_size=pool_size)


def test_empty_database_url_is_rejected() -> None:
    with pytest.raises(ValidationError, match="database_url"):
        Settings(database_url="  ")
