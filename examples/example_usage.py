# examples/example_usage.py

from pyutils import log_calls, retry, time_execution


@log_calls
@time_execution
def compute_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


@retry(attempts=3, delay=0.5)
def unstable_function():
    import random

    if random.random() < 0.7:
        raise ValueError("Random failure occurred!")

    return "Success!"


if __name__ == "__main__":
    print("Running compute_sum...")
    print(compute_sum(10000))

    print("\nRunning unstable_function...")
    try:
        print(unstable_function())
    except Exception as e:
        print("Final failure:", e)