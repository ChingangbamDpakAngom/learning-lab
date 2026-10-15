"""NumPy brush-up (W2): exercises first, look up only what you've forgotten.

Setup once (NumPy is a runtime dependency, so no --dev):
    uv add numpy
Run from the repo root:
    uv run python drill/numpy/numpy_brushup.py

Data: prescription items (thousands) for 4 months (rows) x 3 regions (columns).
Write each step's code under its "# Step n" marker in main() and print the result.

Step 1. Inspect: print items.shape, items.ndim, items.dtype, items.size.
        Expected: (4, 3)  2  int64  12
Step 2. Index + slice: month 1 (row 0); region B (column 1); month 3 region C; the last 2 months.
        Expected: [120 80 95] · [80 85 90 70] · 105 · [[110 90 105] [140 70 98]]
Step 3. Vectorise (no loops): cost at £8.50 per item; month-on-month % change (np.diff on axis 0).
        Expected first % row: [8.33 6.25 5.26] (round to 2 dp)
Step 4. Aggregate with axis: total per region; mean per month; which region (index) has the biggest total.
        Expected: [500 325 398] · [98.33 105. 101.67 102.67] · 0
Step 5. Boolean mask: all values above 100, how many there are, and a "high"/"normal" label array (np.where).
        Expected: [120 130 110 105 140] in row order → count 5
Step 6. Broadcasting: z-score every column in one line: (x - column mean) / column std.
        Check: each column of the result has mean ≈ 0 (use np.allclose).
Step 7. Reshape + stack: add month 5 = [125, 88, 102] with np.vstack; then flatten it.
        Expected: shape (5, 3), then 15 values
Step 8. Stats: median and 90th percentile of all values; unique BNF chapters with their counts.
        Expected: median 99.0 · p90 129.0 · chapters ['cardio' 'resp' 'skin'] counts [2 1 2]
Step 9. Cosine similarity (you'll use this for embeddings in W4): a @ b / (norm(a) * norm(b)).
        Expected: cos(a, b) = 1.0 · cos(a, c) ≈ 0.0845
Step 10. (Stretch) Time a Python loop sum vs np.sum on 1,000,000 numbers with time.perf_counter.
"""

import numpy as np

items = np.array([
    [120, 80, 95],
    [130, 85, 100],
    [110, 90, 105],
    [140, 70, 98],
])
chapters = np.array(["cardio", "resp", "cardio", "skin", "skin"])
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
c = np.array([3, -1, 0])


def main() -> None:
    # Step 1 : inspecting array
    print(f"""shape: {items.shape}, 
              Dimension:{items.ndim},
              type: {items.dtype}, 
              number of items: {items.size}""")


    # Step 2 : index and slicing
    print(f"""Month:{items[0,:]} 
          Region B: {items[:,1]}
          Month 3, region C: {items[2,2]}
          The last 2 month: {items[2:,:]} """)


    # Step 3 : Maths without loops
    cost = items*8.5
    change = np.diff(items, axis = 0) 
    previous_month = items[:-1, :]
    percentage = (change /previous_month *100).round(2)

    print(f"""
    cost of every value at £8.50 per item: {cost} 
    Month on month % changes: 0{percentage}
    """)

    # Step 4 : Total and averages with axis
    total_per_region = np.sum(items, axis = 0)
    average_per_month = (np.sum(items, axis = 1)/len(items[0,:]))
    biggest_total_index =  total_per_region.argmax()

    print(f"""  {total_per_region}
                {average_per_month}
                {biggest_total_index}""")

    # Step 5 : Filter with a condition
    values_above_100 = np.where(items >100)
    how_many = len(values_above_100)
    same_shape = np.where(items>100, "Hihg", "Low")

    print(f"""
        {values_above_100}
        {how_many}
        {same_shape}
""")

    # Step 6

    # Step 7

    # Step 8

    # Step 9

    # Step 10
    ...


if __name__ == "__main__":
    main()
