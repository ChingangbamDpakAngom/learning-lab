"""Code under test for the pytest drill. Complete: you only write the tests."""
import csv
from pathlib import Path


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


def save_totals(rows, out_path):
    """Write rows like [("2026-09", 120), ...] to a CSV and return the path."""
    out_path = Path(out_path)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "items"])
        writer.writerows(rows)
    return out_path
