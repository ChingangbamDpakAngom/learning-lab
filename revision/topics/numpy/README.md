# NumPy

**Status:** ⏳ brush-up in progress (learned before, functions forgotten) · **Sessions:** 15 Oct (W2 brush-up) · **Code:** [`drill/numpy/numpy_brushup.py`](../../../drill/numpy/numpy_brushup.py)
**Cheat sheet:** [NumPy for AI Engineers](NumPy-Cheat-Sheet.jpg) (the ~60 names used day to day, AI recipes, gotchas) · **Interview Qs:** none yet
**Resources:** [100 NumPy exercises](https://github.com/rougier/numpy-100) #1–30 · [PDSH ch. 2](https://jakevdp.github.io/PythonDataScienceHandbook/) for lookups only

## Must know (fill in as the drill goes)
- Inspect: `shape`, `ndim`, `dtype`, `size`.
- Index + slice: `a[row, col]`, `a[:, 1]`, `a[-2:]`.
- Vectorise: maths on whole arrays, no Python loops (much faster).
- `axis=0` = down the rows (per column) · `axis=1` = across columns (per row).
- Boolean mask `a[a > 100]`, `np.where(cond, x, y)`.
- Broadcasting: `(x - x.mean(axis=0)) / x.std(axis=0)`.
- Reshape + stack: `reshape`, `np.vstack`, `flatten`.
- Stats: `np.median`, `np.percentile`, `np.unique(..., return_counts=True)`.
- Cosine similarity: `a @ b / (norm(a) * norm(b))` (embeddings, W4).

## Mistakes I made
- Inspected the wrong array (`a`, shape `(3,)`) instead of `items` `(4, 3)`: always check `.shape` first.
- `{:,1}` in an f-string: the array name is required, `{items[:, 1]}`. Keep maths out of f-strings; use variables.
- `items.diff(...)`: `diff` is a function, `np.diff(items, axis=0)`.
- Average per month: used `axis=0` (that is per region), then divided by `len(items)` (rows = 4, not 3). Use `items.mean(axis=1)`.
- `np.where(max(x))` for the biggest position: `max` gives the value, `argmax` gives the position.
- `np.where(cond)` alone returns positions; the values are `items[items > 100]`, the count is `(items > 100).sum()`.
- Z-score without `axis=0` used one global mean, so whole columns were all positive or all negative.

## Gaps
- [x] Drill steps 1–8. [ ] Steps 9 (cosine) and 10 (speed test).
- [ ] Views vs copies: slicing returns a **view**, so editing it changes the original; use `.copy()`. Classic gotcha.
- [ ] `np.random.default_rng(seed)` for reproducible data.
- [ ] dtype gotcha: assigning 2.7 into an int array silently stores 2.
- [x] Cheat sheet. [ ] Topic card + interview Qs when done.
- [ ] Revisit in W6 (ML fundamentals) → update this file, not a new one.
