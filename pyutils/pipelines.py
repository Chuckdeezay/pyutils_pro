# pyutils/pipelines.py

from typing import Iterable, Generator


# -------------------------
# STEP 1: FILTERING STAGE
# -------------------------
def filter_errors(
    lines: Iterable[str]
) -> Generator[str, None, None]:
    """
    Keeps only lines that contain 'ERROR'.
    """

    for line in lines:
        if "ERROR" in line:
            yield line


# -------------------------
# STEP 2: TRANSFORM STAGE
# -------------------------
def extract_timestamps(
    lines: Iterable[str]
) -> Generator[str, None, None]:
    """
    Extracts timestamp from log line.

    Assumes format:
    timestamp | level | message
    """

    for line in lines:
        yield line.split("|")[0].strip()


# -------------------------
# STEP 3: CLEANING STAGE
# -------------------------
def clean_lines(
    lines: Iterable[str]
) -> Generator[str, None, None]:
    """
    Removes empty or whitespace-only lines.
    """

    for line in lines:
        cleaned = line.strip()
        if cleaned:
            yield cleaned