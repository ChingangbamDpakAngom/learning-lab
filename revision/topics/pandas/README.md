# pandas

**Status:** ⏳ brush-up in progress (learned before, functions forgotten) · **Sessions:** 16 Oct (W2 brush-up) · **Code:** [`drill/pandas/pandas_brushup.py`](../../../drill/pandas/pandas_brushup.py)
**Cheat sheet:** [pandas for AI Engineers](Pandas-Cheat-Sheet.jpg) · **Interview Qs:** none yet
**Resources:** [Kaggle Learn Pandas](https://www.kaggle.com/learn/pandas) for lookups only (exercise first)

## Must know (interview depth)
- Inspect first: `shape`, `info()`, `isna().sum()`, `duplicated().sum()`, `value_counts()`.
- Clean: `drop_duplicates`, `dropna` vs `fillna` (a judgement call), `.str.strip().str.lower()`, `pd.to_numeric(errors="coerce")`, `pd.to_datetime(format=...)`.
- Filter: `df[(c1) & (c2)]` with brackets, `.loc[mask, cols]`, `isin`.
- `groupby(...).agg(name=("col", "func"))`, `sort_values`, `transform`.
- `merge(how="left")` and **check the row count after**; `concat`; `pivot_table`.
- AI uses: eval results per model, p95 latency, JSONL logs (`read_json(lines=True)`), table → text column for embeddings.

## Mistakes I made
- (add as the drill goes)

## Gaps
- [ ] Drill steps 1–13.
- [ ] Lab 03: clean + profile a real dataset.
- [ ] Topic card + interview Qs when done.
- [ ] Revisit with DuckDB / SQL comparisons (SQL Saturday) → update this file, not a new one.
