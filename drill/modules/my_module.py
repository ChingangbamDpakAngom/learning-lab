"""A tiny module to import (Corey Schafer: Import Modules and the Standard Library)."""

print("Imported my_module...")   # top-level code runs once, on the first import

test = "Test String"


def find_index(to_search, target):
    """Return the index of target in to_search, or -1 if it's not there."""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
