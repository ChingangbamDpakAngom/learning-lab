# SQL

**Status:** 🟡 part 1 only · **Sessions:** [28 Sep, part 1](../../../log/2026-09-28_w1-d1/notes.md) · **Code:** [`drill/sql/`](../../../drill/sql) (empty so far) · **Playground:** https://shell.duckdb.org
**Interview Qs:** none yet

## Must know (part 1)
- DBMS = stores data + answers queries (PostgreSQL, MySQL, SQLite, DuckDB). Relational = tables of rows × typed columns; primary key = unique row id; NULL = unknown (not 0, not "").
- Declarative: say *what*, the database decides *how*. Runs inside the DB → handles data bigger than RAM (pandas loads it all).
- `SELECT cols / * / expr AS name / DISTINCT` · `WHERE` with `AND/OR`, `IN`, `BETWEEN` (inclusive), `LIKE 'O%'`, `IS NULL` (never `= NULL`).
- `ORDER BY col DESC`, `LIMIT n` (`LIMIT 3 OFFSET 3` = `[3:6]`). No built-in order → LIMIT without ORDER BY is arbitrary. `NULLS LAST`.
- pandas map: WHERE = boolean mask · ORDER BY = `sort_values` · LIMIT = `head` · DISTINCT = `unique` · GROUP BY = `groupby` · JOIN = `merge`.

## Mistakes I made
- None recorded yet.

## Gaps
- [ ] Part 2: GROUP BY / HAVING, `COUNT(*)` vs `COUNT(col)` (SQL Saturday, 17 Oct).
- [ ] Logical order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT (why WHERE can't use an aggregate or a SELECT alias). Top interview question.
- [ ] Joins (INNER vs LEFT, where NULLs appear), CTEs (`WITH`), window functions (ROW_NUMBER, RANK, LAG, running totals).
- [ ] Practice: SQLBolt 6–12 → PostgreSQL Exercises "Joins" + "Aggregates" → DataLemur easy. `drill/sql/` is still empty.
- [ ] Cheat sheet + interview Qs once part 2 is done.
