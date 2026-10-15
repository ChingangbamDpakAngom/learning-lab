# Topics: one file per topic

Everything I know about a topic, in one file, however many days or weeks I studied it.
`log/` stays the day-by-day diary; these files are the **compiled** version for revision and gap checks.

**Rule:** when I study a topic again (e.g. NumPy in W2 and again in W5), the same file is updated: new points merged into *Must know*, the session added to *Sessions*, gaps ticked or added. Never a second file.

Each file has the same parts:
- **Status · Sessions · Code · Cheat sheet · Interview Qs**: where everything lives
- **Must know**: the core points, interview depth
- **Mistakes I made**: from quizzes and recall checks
- **Gaps**: not done yet, skipped on purpose, or still shaky

| Topic | Status | Last studied | Open gaps |
|---|---|---|---|
| [DSA: Big-O + two pointers](dsa.md) | ✅ | 25 Sep | NeetCode backlog; fast/slow pointers (W4) |
| [Descriptive statistics](statistics.md) | ✅ theory | 25 Sep | practical pending; p-values + A/B (W6) |
| [Docker + Redis](docker-redis.md) | 🟡 theory only | 25 Sep | hands-on `docker run` + `redis-cli` not done |
| [Python core](python-core.md) | ✅ | 28 Sep | generators, decorators, `*args/**kwargs`, GIL |
| [Errors, file I/O, retries](errors-files.md) | ✅ | 2 Oct | used for real in lab 01 |
| [Logging](logging.md) | ✅ | 3 Oct | handlers/formatters (concept only) |
| [Modules, imports, environments](modules-imports.md) | ✅ | 6 Oct | — |
| [OOP + dataclasses](oop.md) | ✅ | 8 Oct | PYnative exercises; `__post_init__` shaky |
| [pytest](pytest.md) | ✅ | 8 Oct | conftest, scopes, coverage (W3) |
| [Git](git.md) | 🟡 | 10 Oct | merge conflict + pull request (lab 01) |
| [argparse (CLI)](argparse.md) | ✅ | 15 Oct | subcommands (skipped) |
| [SQL](sql.md) | 🟡 part 1 | 28 Sep | GROUP BY/HAVING, joins, CTEs, windows |
| [NumPy](numpy.md) | ⏳ brush-up | 15 Oct | drill steps 1–10 |

Status: ✅ done to interview depth · 🟡 partly done · ⏳ in progress.
Not started yet: pandas · lab 03 · W3 onwards. A file is created the first day a topic is studied.
