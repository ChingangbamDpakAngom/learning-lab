# Topics: one folder per topic

Everything I know about a topic, in one folder, however many days or weeks I studied it.
`log/` stays the day-by-day diary; these folders are the **compiled** version for revision and gap checks.

**Rule:** when I study a topic again (e.g. NumPy in W2 and again in W5), the same folder is updated: new points merged into *Must know*, the session added to *Sessions*, gaps ticked or added. Never a second folder.

Each folder holds:
- `README.md`: **Status · Sessions · Code · Cheat sheet · Interview Qs** → **Must know** (interview depth) → **Mistakes I made** → **Gaps** (not done, skipped on purpose, or shaky)
- `<Topic>-Cheat-Sheet.jpg` + its `.source.html` (render: `python log/assets/render.py revision/topics/<topic>/<Topic>-Cheat-Sheet.source.html`)
- `Interview-Questions.md` when the topic has its own question set

| Topic | Status | Last studied | Cheat sheet | Biggest open gaps |
|---|---|---|---|---|
| [DSA: Big-O + two pointers](dsa/README.md) | ✅ | 25 Sep | ✅ ×2 | NeetCode docstrings blank; arrays & hashing notes; next patterns |
| [Descriptive statistics](statistics/README.md) | ✅ theory | 25 Sep | ✅ | practical; probability + distributions; p-values (W6) |
| [Docker + Redis](docker-redis/README.md) | 🟡 theory only | 25 Sep | ❌ | hands-on never done; production Dockerfile (W7) |
| [Python core](python-core/README.md) | ✅ | 28 Sep | ✅ | `*args/**kwargs`, generators, decorators, GIL, custom context managers |
| [Errors, file I/O, retries](errors-files/README.md) | ✅ | 2 Oct | ✅ | `timeout=` + `raise_for_status()`; lab 01 |
| [Logging](logging/README.md) | ✅ | 3 Oct | ✅ | handlers/formatters in code |
| [Modules, imports, environments](modules-imports/README.md) | ✅ | 6 Oct | ✅ | — (use in lab 01) |
| [OOP + dataclasses](oop/README.md) | ✅ | 8 Oct | ✅ | composition vs inheritance; type hints + Pydantic; PYnative |
| [pytest](pytest/README.md) | ✅ | 8 Oct | ❌ | test discovery + flags; monkeypatch |
| [Git](git/README.md) | 🟡 | 10 Oct | ❌ | conflict + PR (lab 01); **shell basics not started** |
| [argparse (CLI)](argparse/README.md) | ✅ | 15 Oct | ❌ | lab 01 |
| [SQL](sql/README.md) | 🟡 part 1 | 28 Sep | ❌ | GROUP BY, logical order, joins, CTEs, windows |
| [NumPy](numpy/README.md) | ⏳ brush-up | 15 Oct | ❌ | drill 1–10; views vs copies |

Status: ✅ done to interview depth · 🟡 partly done · ⏳ in progress.
Not started yet: pandas · type hints + Pydantic (W3) · shell basics · lab 03 · W3 onwards. A folder is created the first day a topic is studied.
