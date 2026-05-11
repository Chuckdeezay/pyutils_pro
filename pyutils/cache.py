# pyutils/cache.py

import time

from collections import OrderedDict
from functools import wraps, lru_cache
from typing import Callable, Any, Dict, Tuple


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def make_key(args: Tuple[Any, ...], kwargs: dict) -> Tuple:
    """
    Converts function arguments into a hashable cache key.
    """

    kwargs_items = tuple(sorted(kwargs.items()))
    return args + kwargs_items


# =========================================================
# BASIC MEMOIZATION
# =========================================================

def memoize(func: Callable) -> Callable:
    """
    Simple memoization decorator.
    """

    cache: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        key = make_key(args, kwargs)

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    return wrapper


# =========================================================
# TTL CACHE
# =========================================================

def ttl_cache(ttl_seconds: int = 60):
    """
    Time-based cache decorator.
    """

    def decorator(func):

        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):

            key = make_key(args, kwargs)

            current_time = time.time()

            # Check cache
            if key in cache:

                result, timestamp = cache[key]

                # Validate TTL
                if current_time - timestamp < ttl_seconds:
                    return result

            # Cache miss OR expired
            result = func(*args, **kwargs)

            cache[key] = (result, current_time)

            return result

        return wrapper

    return decorator


# =========================================================
# MANUAL INVALIDATION CACHE
# =========================================================

def memoize_with_invalidation(func: Callable) -> Callable:
    """
    Memoization decorator with manual invalidation support.
    """

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        key = make_key(args, kwargs)

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    def clear_cache():
        cache.clear()

    wrapper.clear_cache = clear_cache

    return wrapper


# =========================================================
# BUILT-IN LRU CACHE EXAMPLE
# =========================================================

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """
    Recursive Fibonacci with LRU caching.
    """

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# =========================================================
# CUSTOM LRU CACHE
# =========================================================

class SimpleLRUCache:
    """
    Simplified LRU cache implementation.
    """

    def __init__(self, capacity: int = 3):

        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return None

        # Move item to end (recently used)
        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        # Move existing item to end
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Remove oldest item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def display(self):

        print(self.cache)