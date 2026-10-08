# Week 2 finish + revision plan (Thu 8 – Sun 11 Oct)

**Where I am:** about 2 days behind plan v4.2. Sunday is light because of the M&S induction at 6 am.

| Done this week ✅ | Still open ⏳ |
|---|---|
| Modules, imports, `-m`, `-e`, uv | Git basics · argparse (CLI) |
| OOP + 4 pillars | **Lab 01**: NHSBSA downloader + CLI + tests |
| Dataclasses vs Pydantic | NumPy · pandas |
| pytest: 16 tests (fixtures, raises, parametrize, tmp_path, mocker) | SQL: GROUP BY/HAVING, joins, CTEs, window functions |
| | Lab 03 (clean + profile a dataset) · Python Qs: generators, decorators, `*args/**kwargs`, GIL |

**Order rule:** git → argparse → lab 01 uses them right away. NumPy → pandas → lab 03 uses them. SQL runs on Saturday, as in the plan.

---

## Fri 9 Oct · CLI + git + lab 01 (full day)
| # | Task | Read / watch (only these parts) | Time |
|---|---|---|---|
| 1 | 🔁 Warm-up revision | [Topic Cards](https://claude.ai/artifact/FQhbAeERhqnSYSBS7UgVpK) recall mode: modules + OOP (weak spots first) | 20 m |
| 2 | Git basics | Corey Schafer [Git Tutorial for Beginners](https://www.youtube.com/watch?v=HVsySz-h9r4) (whole) · [MIT Missing Semester](https://missing.csail.mit.edu/) "Version Control (Git)" lecture: watch the first 30 min | 1 h |
| 3 | Git practice | In a scratch repo, do one round each: branch → commit → merge, then make a conflict and resolve it; write `.gitignore` | 30 m |
| 4 | argparse | Python docs [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html): up to "Combining positional and optional arguments" | 45 m |
| 5 | **Lab 01** | NHSBSA downloader + CLI + tests. Uses requests, argparse, logging, retries and pytest-mock. Say `start lab 01` in a fresh chat | 3 h |
| 6 | NeetCode | 1 problem from the backlog (Two Sum / Group Anagrams) | 30 m |
| 7 | Close | 5-min blurt, then a `LEARNED.md` entry + topic cards (git, argparse) | 15 m |

## Sat 10 Oct · NumPy + pandas + SQL Saturday
| # | Task | Read / watch (only these parts) | Time |
|---|---|---|---|
| 1 | 🔁 Warm-up revision | The 3 self-check questions in the [pytest explainer](explainers/pytest-raises-parametrize-mocker.md) + dataclass `__post_init__` (weak spot) | 20 m |
| 2 | NumPy | [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) ch. 2: arrays + dtypes, computation on arrays (vectorisation), aggregations, broadcasting | 1.5 h |
| 3 | pandas | [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas): all 6 lessons (read/write, select, summary + map, groupby + sort, dtypes + missing values, rename + merge). Corey Schafer's [pandas playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) only where you get stuck | 2.5 h |
| 4 | SQL Saturday | GROUP BY + HAVING, joins, CTEs (`WITH`): [Kaggle Intro to SQL](https://www.kaggle.com/learn/intro-to-sql), the lessons "Group By, Having & Count", "As & With" and "Joining Data". Then 2 easy problems on [DataLemur](https://datalemur.com/) | 1.5 h |
| 5 | Close | Blurt, `LEARNED.md` entry + topic cards (NumPy, pandas, SQL) | 15 m |

## Sun 11 Oct · light day: weekly review (after the induction)
| # | Task | Time |
|---|---|---|
| 1 | **Weekly revision session** (checklist below) | 1.5 h |
| 2 | *If you have energy:* window functions with [Kaggle Advanced SQL](https://www.kaggle.com/learn/advanced-sql), lesson "Analytic Functions" (ROW_NUMBER, RANK, LAG, running totals) | 45 m |
| 3 | Plan W3 with Claude | 10 m |

## Moves to W3 Mon 12 Oct (catch-up morning, before FastAPI)
- **Lab 03:** clean + profile a dataset with pandas (nulls, dtypes, duplicates). About 2 h.
- **Python interview Qs:** generators, decorators, `*args/**kwargs`, the GIL. About 20 min each, learned in chat.
- SQL window functions, if you skipped them on Sunday.

---

## Revision plan

**Every study day:** a 20-min warm-up before new work: recall mode on 2 topics, weakest first. Rate them Shaky / OK / Solid.

**Spaced repeats:** review each topic on day 1, day 3 and day 7 after learning it.
| Learned | Day 3 review | Day 7 review |
|---|---|---|
| Modules + uv (6 Oct) | Fri 9 ✔ in the warm-up | Mon 13 |
| OOP (7 Oct) | Sat 10 | Tue 14 |
| Dataclasses + pytest (8 Oct) | Sat 10 ✔ in the warm-up | Wed 15 |
| Git + argparse + lab 01 (9 Oct) | Mon 12 | Fri 16 |
| NumPy + pandas + SQL (10 Oct) | Tue 13 | Sat 17 |

**Sunday weekly review (1.5 h), in order:**
1. **W2 deep** (45 m). For each topic: open the card in recall mode → say What · Why · How · Solves · When **out loud** → reveal → rate it.
   Topics: modules → uv → OOP → dataclasses → pytest → git → argparse → NumPy → pandas → SQL.
2. **Interview questions** (20 m): answer 10 from the [29 OOP Qs](../log/2026-10-06_w2-d2/OOP-Interview-Questions.md) and the pytest section of [INTERVIEW-QA.md](INTERVIEW-QA.md) out loud.
3. **W0–W1 quick pass** (15 m), one line each: Big-O (time **and** space), Python core, errors + retries, logging.
4. **Quiz with Claude** (10 m): `Quiz` in the revision Project ([CONTEXT.md](CONTEXT.md)).
5. **Log it:** every Shaky card or missed question goes into [weak-spots.md](../log/weak-spots.md) → re-test on day 3.

**Done when** every W2 card is OK or Solid, and you can explain lab 01 end to end in 2 minutes (what it downloads, how the CLI works, how it's tested).
