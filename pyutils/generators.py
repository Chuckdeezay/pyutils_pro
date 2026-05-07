# pyutils/generators.py

from typing import Generator


class CountUpTo:
    """
    Manual iterator implementation.
    """

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


# -------------------------
# GENERATOR FUNCTIONS
# -------------------------

def count_up_to(limit: int):
    """
    Generator version of CountUpTo.
    """

    current = 1

    while current <= limit:
        yield current
        current += 1


def read_large_file(
    filepath: str
) -> Generator[str, None, None]:
    """
    Lazily reads a file line-by-line.
    """

    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()