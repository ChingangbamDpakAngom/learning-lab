# NumPy

**Status:** ⏳ brush-up in progress (learned before, functions forgotten) · **Sessions:** 15 Oct (W2 brush-up) · **Code:** [`drill/numpy/numpy_brushup.py`](../../../drill/numpy/numpy_brushup.py)
**Cheat sheet:** to make from whatever I had to look up · **Interview Qs:** none yet
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
- (add as the drill goes)

## Gaps
- [ ] Drill steps 1–10.
- [ ] Views vs copies: slicing returns a **view**, so editing it changes the original; use `.copy()`. Classic gotcha.
- [ ] `np.random.default_rng(seed)` for reproducible data.
- [ ] dtype gotcha: assigning 2.7 into an int array silently stores 2.
- [ ] Cheat sheet + topic card + interview Qs when done.
- [ ] Revisit in W6 (ML fundamentals) → update this file, not a new one.
