# examples/example_usage.py

"""
from pyutils.cache import (
    memoize,
    ttl_cache,
    fibonacci,
    SimpleLRUCache,
    memoize_with_invalidation,
)


# =========================================================
# BASIC MEMOIZATION
# =========================================================

@memoize
def expensive_sum(n: int) -> int:

    print("Computing expensive sum...")

    return sum(range(n))


# =========================================================
# TTL CACHE
# =========================================================

@ttl_cache(ttl_seconds=5)
def get_data():

    print("Fetching fresh data...")

    return {"status": "success"}


# =========================================================
# MANUAL INVALIDATION
# =========================================================

@memoize_with_invalidation
def expensive_operation(x):

    print("Running expensive operation...")

    return x * 10


# =========================================================
# MAIN EXECUTION
# =========================================================

if __name__ == "__main__":

    print("\n--- BASIC MEMOIZATION ---")
    print(expensive_sum(10000))
    print(expensive_sum(10000))

    print("\n--- TTL CACHE ---")
    print(get_data())
    print(get_data())

    print("\n--- LRU CACHE (FIBONACCI) ---")
    print(fibonacci(35))

    print("\n--- CUSTOM LRU CACHE ---")

    cache = SimpleLRUCache(capacity=3)

    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)

    cache.display()

    cache.get("A")

    cache.put("D", 4)

    cache.display()

    print("\n--- MANUAL INVALIDATION ---")

    print(expensive_operation(5))
    print(expensive_operation(5))

    expensive_operation.clear_cache()

    print(expensive_operation(5))


# examples/example_usage.py

from pyutils.context_managers import (
    FileManager,
    file_manager,
    transaction,
    multiple_files,
)


if __name__ == "__main__":

    # =====================================================
    # CLASS-BASED CONTEXT MANAGER
    # =====================================================
    print("\n--- CLASS-BASED FILE MANAGER ---")

    with FileManager("sample1.txt", "w") as f:
        f.write("Hello from class-based context manager\n")


    # =====================================================
    # GENERATOR-BASED CONTEXT MANAGER
    # =====================================================
    print("\n--- GENERATOR-BASED FILE MANAGER ---")

    with file_manager("sample2.txt", "w") as f:
        f.write("Hello from generator-based context manager\n")


    # =====================================================
    # TRANSACTION DEMO (SUCCESS)
    # =====================================================
    print("\n--- TRANSACTION SUCCESS ---")

    with transaction("UserUpdate"):
        print("Updating user...")
        print("Saving changes...")


    # =====================================================
    # TRANSACTION DEMO (FAILURE)
    # =====================================================
    print("\n--- TRANSACTION FAILURE ---")

    try:
        with transaction("Payment"):
            print("Charging user...")
            raise Exception("Payment failed!")

    except Exception:
        print("Exception handled outside transaction")


    # =====================================================
    # MULTI-FILE CONTEXT MANAGER
    # =====================================================
    print("\n--- MULTIPLE FILES (ExitStack) ---")

    with multiple_files("a.txt", "b.txt", "c.txt", mode="w") as files:

        for i, f in enumerate(files):
            f.write(f"File {i} written via ExitStack\n")

    print("All files safely closed")
"""
# examples/example_usage.py

from pyutils.models import (
    User,
    UserFormatter,
    Account,
    Product,
)

from pyutils.collections import UserGroup


if __name__ == "__main__":

    # =====================================================
    # USER MODEL
    # =====================================================

    print("\n--- USER MODEL ---")

    user = User(
        1,
        "Charles",
        "charles@email.com"
    )

    print(user)

    # =====================================================
    # DICT-LIKE ACCESS
    # =====================================================

    print("\n--- DICT-LIKE ACCESS ---")

    print(user["email"])

    user["name"] = "Charles Shaw"

    print(user)

    # =====================================================
    # MEMBERSHIP TEST
    # =====================================================

    print("\n--- MEMBERSHIP TEST ---")

    print("email" in user)

    # =====================================================
    # SORTING USERS
    # =====================================================

    print("\n--- SORTING USERS ---")

    users = [
        User(3, "C", "c@email.com"),
        User(1, "A", "a@email.com"),
        User(2, "B", "b@email.com"),
    ]

    print(sorted(users))

    # =====================================================
    # CALLABLE OBJECT
    # =====================================================

    print("\n--- CALLABLE OBJECT ---")

    formatter = UserFormatter()

    print(formatter(user))

    # =====================================================
    # CUSTOM COLLECTION
    # =====================================================

    print("\n--- CUSTOM COLLECTION ---")

    group = UserGroup(users)

    for u in group:
        print(u)

    print(f"Total users: {len(group)}")

    # =====================================================
    # PROPERTY EXAMPLE
    # =====================================================

    print("\n--- PROPERTY EXAMPLE ---")

    account = Account("Charles", 1000)

    print(account.balance)

    account.balance = 1500

    print(account.balance)

    # =====================================================
    # DESCRIPTOR EXAMPLE
    # =====================================================

    print("\n--- DESCRIPTOR EXAMPLE ---")

    product = Product(
        "Laptop",
        2500,
        5
    )

    print(product)

    try:
        product.price = -100

    except ValueError as e:
        print(e)