from pyutils.generators import read_large_file
from pyutils.pipelines import filter_errors, extract_timestamps


def main():
    # Step 1: lazy file read
    lines = read_large_file("sample.log")

    # Step 2: inline transformation (generator expression)
    cleaned = (line.strip() for line in lines if line.strip())

    # Step 3: pipeline stages
    errors = filter_errors(cleaned)
    timestamps = extract_timestamps(errors)

    # Step 4: consume stream
    for ts in timestamps:
        print(ts)


if __name__ == "__main__":
    main()