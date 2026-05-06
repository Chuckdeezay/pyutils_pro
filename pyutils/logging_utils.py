# pyutils/logging_utils.py

import logging
from typing import Optional


def setup_logger(
    name: str = "pyutils",
    level: int = logging.INFO
) -> logging.Logger:
    """
    Creates and configures a reusable logger.

    Prevents duplicate handlers and avoids re-configuring
    logging across multiple modules.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers (common pitfall)
    if logger.handlers:
        return logger

    logger.setLevel(level)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


# Global shared logger instance (convenience)
logger = setup_logger("pyutils")


def log_info(message: str, logger_name: Optional[str] = None) -> None:
    """
    Logs an info-level message using a shared or named logger.
    """

    log = logging.getLogger(logger_name or "pyutils")
    log.info(message)


def log_error(message: str, logger_name: Optional[str] = None) -> None:
    """
    Logs an error-level message using a shared or named logger.
    """

    log = logging.getLogger(logger_name or "pyutils")
    log.error(message)