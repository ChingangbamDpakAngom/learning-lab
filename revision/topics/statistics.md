# Descriptive statistics

**Status:** ✅ theory · **Sessions:** [25 Sep](../../log/2026-09-25_w0-d1/notes.md) · **Code:** [`drill/stats/describe.py`](../../drill/stats/describe.py)
**Cheat sheet:** [Descriptive stats](../../log/2026-09-25_w0-d1/Descriptive-Statistics-Cheat-Sheet.jpg) · **Interview Qs:** [day 1 set §3](../../log/2026-09-25_w0-d1/Interview-Questions.md) · [short answers](../INTERVIEW-QA.md#descriptive-statistics)

## Must know
- Centre: mean (pulled by outliers) vs **median** (robust) vs mode (categories). Skewed data → report the median.
- Spread: variance = average squared deviation; **SD** = √variance, in original units. Sample → divide by n−1 (`np.var` ddof=0 vs pandas ddof=1!). Range is fragile; **IQR** = Q3 − Q1 is robust.
- Outliers: beyond Q1 − 1.5·IQR or Q3 + 1.5·IQR (box plot); |z| > 3 for roughly normal data.
- Shape: histogram first. Right skew → mean > median (income, latency).
- z = (x − mean)/SD → what StandardScaler does.
- Production: latency p50/p95/p99, CV results as mean ± SD, drift = comparing distributions.

## Mistakes I made
- None recorded yet (no quiz on this topic).

## Gaps
- [ ] Practical: 1,000 random numbers → mean, median, SD, histogram (NumPy drill step 8 covers part of it).
- [ ] p-values, A/B tests (W6).
