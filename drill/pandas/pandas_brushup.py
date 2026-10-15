"""pandas brush-up (W2): exercises first, look up only what you've forgotten.

Setup once (runtime dependency, so no --dev):
    uv add pandas
Run from the repo root:
    uv run python drill/pandas/pandas_brushup.py

Data: drill/pandas/prescriptions.csv is messy on purpose (like real NHS exports):
a duplicate row, missing items, regions with extra spaces and mixed case, cost as "£1020.00" text.
drill/pandas/regions.csv maps region -> region_code (one region is missing on purpose).
Write each step under its "# Step n" marker in main() and print the result.

--- Load + inspect ---
Step 1. Read prescriptions.csv (encoding="utf-8"). Print shape, dtypes, and the first 3 rows (head).
        Expected: (12, 6) · items is float64 (because of the blanks) · cost is text
Step 2. Count missing values per column (isna + sum) and duplicate rows (duplicated + sum).
        Expected: items has 2 missing · 1 duplicate row

--- Clean ---
Step 3. Drop the duplicate row. Clean region: strip spaces + lowercase (.str methods).
        Expected: 11 rows · regions ['london' 'midlands' 'north west' 'south west']
Step 4. Fix types: cost -> float (remove "£" first), month -> datetime (pd.to_datetime, format="%Y-%m"),
        items: fill missing with 0, then make it int.
        Expected: dtypes cost float64, month datetime64, items int64 · items total 905

--- Select + filter ---
Step 5. Rows where region is london AND items > 90 (use & and brackets). Print practice + items only.
        Expected: 3 rows: P003, P005, P005
Step 6. With .loc: practice and items columns for chapters Resp or Skin (.isin).
        Expected: shape (6, 2)

--- New columns ---
Step 7. cost_per_item = cost / items, but only where items > 0 (otherwise NaN; look up Series.where).
        Expected: 8.5 everywhere except the 2 Midlands rows (NaN)

--- Group + summarise ---
Step 8. Per region: total items, total cost, number of distinct practices (groupby + agg with named outputs),
        sorted by total items, biggest first.
        Expected first row: north west · 425 · 3612.5 · 2
Step 9. How many rows per bnf_chapter (value_counts).
        Expected: Cardio 5 · Resp 3 · Skin 3

--- Combine + reshape ---
Step 10. Left-join regions.csv on region. Print the row count before and after, and which region has no code.
         Expected: 11 rows before and after · 'south west' has no region_code (NaN)
Step 11. Pivot table: months as rows, chapters as columns, total items as values (fill missing with 0).
         Expected: 2025-04 -> Cardio 215, Resp 80, Skin 0 · monthly totals [295, 375, 235]

--- AI touch ---
Step 12. Build a "text" column per row for embeddings / RAG, e.g.
         "P001 in north west prescribed 120 cardio items". Print the first one.
Step 13. (Stretch) Save the clean data to drill/pandas/clean.csv without the index.
"""

import pandas as pd

DATA = "drill/pandas/prescriptions.csv"
REGIONS = "drill/pandas/regions.csv"


def main() -> None:
    # Step 1

    # Step 2

    # Step 3

    # Step 4

    # Step 5

    # Step 6

    # Step 7

    # Step 8

    # Step 9

    # Step 10

    # Step 11

    # Step 12

    # Step 13
    ...


if __name__ == "__main__":
    main()
