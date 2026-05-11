# tests/test_cache.py

from pyutils.cache import memoize


@memoize
def square(x):
    return x * x


def test_square():

    assert square(5) == 25
    assert square(10) == 100