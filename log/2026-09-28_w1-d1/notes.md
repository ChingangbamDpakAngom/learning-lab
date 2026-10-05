# Mon 28 Sep 2026 · Week 1, Day 1

## Learn · Python core: functions, data structures, comprehensions ✅
- Default args are evaluated **once**, when `def` runs → `items=[]` is shared across calls. Use `items=None`.
- Names are references: `b = a` doesn't copy. `a.copy()` / `list(a)` = shallow copy; `copy.deepcopy` for nested data.
- list: `a[i]`, `append`, `pop()` O(1) · `x in a`, `insert(0, x)`, `pop(0)` O(n).
- tuple: immutable → hashable → usable as a dict key / set member. Unpacking: `name, cost = row`.
- dict: O(1) average lookup via hashing, insertion-ordered. `.get(k, 0)`, `Counter`, `defaultdict(list)`.
- set: unique items, O(1) `in`, `& | -`.
- Comprehensions `[f(x) for x in xs if cond]`; `( ... )` = lazy generator for big data. Too complex → write a loop.
- Truthiness: `0`, `""`, `[]`, `{}`, `None` are falsy; everything else is truthy. `if n % 2` means "if n is odd".
- Generated: [Python-Core-Cheat-Sheet.jpg](Python-Core-Cheat-Sheet.jpg)

### Quiz: 5 / 7
| # | Question | My answer | Correct |
|---|---|---|---|
| 1 | mutable default `add(1); add(2)` | `[1, 2]` ✅ | `[1, 2]`: one list shared by both calls |
| 2 | `b = a; b.append(3)` | `[1, 2, 3]` ✅ | same list, two names |
| 3 | `{n: n*n for n in range(4) if n % 2}` | "incomplete condition" ❌ | `{1: 1, 3: 9}`: `n % 2` is 1 (truthy) for odd n, 0 (falsy) for even |
| 4 | `d[[1, 2]] = "b"` | errors, keys can't be mutable ✅ | `TypeError: unhashable type: 'list'`. The rule is *hashable*; mutable built-ins aren't hashable |
| 5 | 50k codes, 1M membership checks | set, O(1) ½ | set: O(1) avg per check (O(n) once to build). List: O(n) per check → 1M × 50k = 5·10¹⁰ steps |
| 6 | loop → comprehension | ✅ | `[r["bnf_code"] for r in rows if r["cost"] > 100]` |
| 7 | `sorted(prices.items(), key=lambda kv: kv[1], reverse=True)[:3]` | list of (key, value) tuples, first 3 ½ | the **3 most expensive** items: sorted by value (`kv[1]`), highest first |

**Mistakes to remember:** truthiness (`if n % 2`); always say the cost of the alternative (list O(n)); read `key=` and `reverse=` to say *which* 3.

## Build · 01 NHSBSA downloader: spec ⬜
## Project · Medicines-Value-Monitor ARCHITECTURE.md ⬜
## Drill · SQL Part 1 (first time with SQL/DBMS) ✅
- DBMS = software that stores data + answers queries (PostgreSQL, MySQL, SQLite, DuckDB). Relational = tables of rows × typed columns; primary key = unique row id; NULL = unknown (not 0, not "").
- SQL is declarative: describe *what*, the database decides *how*. Runs inside the DB → handles data bigger than RAM (pandas loads it all into memory).
- `SELECT cols / * / expr AS name / DISTINCT` · `WHERE` with `AND/OR`, `IN`, `BETWEEN` (inclusive), `LIKE 'O%'`, `IS NULL` (never `= NULL`).
- `ORDER BY col DESC` = sort, `LIMIT n` = slice (`LIMIT 3 OFFSET 3` = `[3:6]`). Tables have no built-in order → LIMIT without ORDER BY is arbitrary. NULL sort position differs by DBMS → `NULLS LAST`.
- pandas map: WHERE = boolean mask, ORDER BY = `sort_values`, LIMIT = `head`, DISTINCT = `unique`, GROUP BY = `groupby`, JOIN = `merge`.
- Playground: https://shell.duckdb.org with the 8-row `prescriptions` table.
- Next: Part 2 GROUP BY / HAVING / COUNT vs COUNT(col), then DataLemur: Histogram of Tweets, Laptop vs Mobile Viewership.
## Apply · approach charity 1 ⬜
