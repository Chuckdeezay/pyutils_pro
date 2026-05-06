# pyutils/decorators.py

from functools import wraps
from typing import Callable, Any
import logging
import time

logging.basicConfig(level=logging.INFO)


# -------------------------
# LOGGING DECORATOR
# -------------------------
def log_calls(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"[CALL] {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"[RETURN] {func.__name__} -> {result}")
        return result
    return wrapper


# -------------------------
# RETRY DECORATOR
# -------------------------
def retry(attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None

            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)

            raise last_exception

        return wrapper
    return decorator