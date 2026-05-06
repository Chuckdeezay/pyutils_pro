# tests/test_decorators.py

from pyutils.decorators import log_calls


def test_add():
    @log_calls
    def add(a, b):
        return a + b

    assert add(2, 3) == 5