"""Tests for configured application logging."""

import json
import logging

from demandpilot.logging_config import JsonFormatter, configure_logging
from demandpilot.settings import Settings


def test_json_formatter_emits_level_and_message() -> None:
    record = logging.LogRecord("demandpilot.test", logging.WARNING, "", 0, "hello", (), None)

    output = json.loads(JsonFormatter().format(record))

    assert output["level"] == "WARNING"
    assert output["logger"] == "demandpilot.test"
    assert output["message"] == "hello"
    assert "timestamp" in output


def test_configure_logging_uses_settings() -> None:
    configure_logging(Settings(log_level="DEBUG", log_format="json"))

    root_logger = logging.getLogger()
    assert root_logger.level == logging.DEBUG
    assert len(root_logger.handlers) == 1
    assert isinstance(root_logger.handlers[0].formatter, JsonFormatter)
