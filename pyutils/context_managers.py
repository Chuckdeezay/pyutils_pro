# pyutils/context_managers.py

from contextlib import contextmanager, ExitStack


# =========================================================
# CLASS-BASED CONTEXT MANAGER
# =========================================================

class FileManager:
    """
    Basic class-based context manager.
    """

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file (class-based)...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file (class-based)...")

        if self.file:
            self.file.close()

        return False


# =========================================================
# GENERATOR-BASED CONTEXT MANAGER
# =========================================================

@contextmanager
def file_manager(filename: str, mode: str):
    """
    Generator-based context manager.
    """

    print("Opening file (generator-based)...")

    f = open(filename, mode)

    try:
        yield f
    finally:
        print("Closing file (generator-based)...")
        f.close()


# =========================================================
# TRANSACTION CONTEXT MANAGER
# =========================================================

@contextmanager
def transaction(name: str):
    """
    Simulates a database transaction.
    """

    print(f"START TRANSACTION: {name}")

    try:
        yield
        print(f"COMMIT TRANSACTION: {name}")

    except Exception:
        print(f"ROLLBACK TRANSACTION: {name}")
        raise


# =========================================================
# MULTI-RESOURCE CONTEXT MANAGER
# =========================================================

@contextmanager
def multiple_files(*filenames: str, mode: str = "r"):
    """
    Manages multiple files safely using ExitStack.
    """

    with ExitStack() as stack:

        files = [
            stack.enter_context(open(fname, mode))
            for fname in filenames
        ]

        yield files