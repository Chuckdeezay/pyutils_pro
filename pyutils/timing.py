# pyutils/timing.py

import time
from functools import wraps
from typing import Callable, Any


def time_execution(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"[TIMER] {func.__name__} took {end - start:.6f}s")

        return result

    return wrapper