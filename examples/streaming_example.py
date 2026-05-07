# examples/streaming_example.py

from pyutils.generators import read_large_file
from pyutils.pipelines import (
    filter_errors,
    extract_timestamps,
    clean_lines
)


def main():
    # Step 1: read file lazily
    lines = read_large_file("sample.log")

    # Step 2: clean data
    cleaned = clean_lines(lines)

    # Step 3: filter errors
    errors = filter_errors(cleaned)

    # Step 4: extract timestamps
    timestamps = extract_timestamps(errors)

    # Step 5: consume pipeline
    for ts in timestamps:
        print(ts)


if __name__ == "__main__":
    main()