# Thu 8 Oct 2026 · Week 2, Day 4 (dataclasses)

OOP (Corey 1–4, 6 + 4 pillars) was finished on 7 Oct: see [OOP cheat sheet](../2026-10-06_w2-d2/OOP-Cheat-Sheet.jpg) · [29 OOP questions](../2026-10-06_w2-d2/OOP-Interview-Questions.md).

## Learn · dataclasses ✅
**How to study this:** Concept (no maths). Remember why + when; the syntax is short.
**Video:** [ArjanCodes: This Is Why Python Data Classes Are Awesome](https://www.youtube.com/watch?v=CvQ7e6yUtnw), 0:00–15:00 (skip kw_only / match_args / slots). Code: `drill/oop/dataclasses_basics.py`.

| Topic | Why | How | When |
|---|---|---|---|
| `@dataclass` | data-holding classes need boring boilerplate | writes `__init__`, `__repr__`, `__eq__` from type-hinted fields | config objects, records, results inside your code |
| Defaults | some fields are optional | `active: bool = True` | — |
| `field(default_factory=list)` | `= []` would be one list shared by all objects (OOP 4 trap; dataclass raises `ValueError`) | a fresh list per object | any list/dict default |
| `field(init=False, repr=False)` | some fields are computed, not passed in | hide from `__init__` / `repr` | derived fields |
| `__post_init__` | compute or check fields after init | runs right after the auto `__init__` | `search_string = name + address`, `if pay < 0: raise` |
| `frozen=True` | data that must not change | assignment → `FrozenInstanceError` | settings, keys in dicts/sets |
| `slots=True` | (one-liner) less memory, faster access | — | many small objects |

**Gotcha I hit:** `frozen=True` + a `__post_init__` that sets `self.x` → `FrozenInstanceError`, because the freeze blocks your own assignment too. Fix: compute it as a `@property`, or don't freeze that class.

**Proved in code:** a normal class prints `<Point object at 0x…>` and `Point(1,2) == Point(1,2)` is **False** (identity). A dataclass prints `Point(x=1, y=2)` and `==` is **True** (compares values). Type hints are **labels, not guards**: `InventoryItem("pen", "abc")` is accepted.

## Dataclass vs Pydantic
| | `@dataclass` | Pydantic `BaseModel` |
|---|---|---|
| From | standard library | `uv add pydantic` |
| Types | not checked | **validated + converted** (`"2.5"` → 2.5) |
| JSON | manual | built in |
| Use for | trusted data **inside** my code | untrusted data from **outside**: API requests (FastAPI → 422), LLM structured output, config |

Kid version: dataclass = labelled box (anything fits) · Pydantic = box with a guard.

## Interview questions
> [!question]- Q1 🟢 What does `@dataclass` generate?
> `__init__`, `__repr__` and `__eq__` (compares field values), from the type-hinted fields.

> [!question]- Q2 🟡 Why `field(default_factory=list)` and not `= []`?
> `= []` would be one list shared by every object (the mutable default trap); dataclasses even raise `ValueError`. `default_factory` builds a fresh list per object.

> [!question]- Q3 🟡 What is `__post_init__` for?
> It runs right after the generated `__init__`, to compute fields from other fields or validate them.

> [!question]- Q4 🔴 Dataclass or Pydantic for an API request body?
> Pydantic: outside data can't be trusted, and Pydantic validates and converts it (FastAPI returns 422 on bad input). Dataclass hints aren't checked at runtime.

> [!question]- Q5 🟡 What does `frozen=True` do, and what's the gotcha?
> Makes instances read-only (`FrozenInstanceError` on assignment) and hashable. Gotcha: it also blocks assignments in your own `__post_init__`.

| Q | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Attempt 1 | ✅ | ✅ | ½ | ½ | |

## Setup · uv for learning-lab (pytest) ✅
Ran from the repo root (`/d/portfolio/learning-lab`, same folder as `.git`):
```bash
uv init --bare          # only pyproject.toml
uv add --dev pytest     # creates .venv + uv.lock, pytest in the dev group
uv run pytest drill/testing -v
```
Result: `.venv/` (git-ignored), `pyproject.toml` + `uv.lock` (commit both). `uv run` = no need to activate. VS Code: Ctrl+Shift+P → Python: Select Interpreter → `.venv`.

| Question | Rule |
|---|---|
| `uv init` or `uv init --bare`? | **New empty folder** → `uv init` (adds `main.py`, `.python-version`, README: useful starters). **Existing repo** → `--bare` (only `pyproject.toml`, no clutter). Unsure → `--bare`. |
| `--dev` or not? | Ask: **does my code `import` it to work?** Yes → `uv add requests` (runtime, even while developing). No, it only tests/checks code → `uv add --dev pytest` (also ruff, pytest-cov, mypy). |
| Why separate them? | Dev tools aren't needed to run the app, so production / Docker installs stay small. |
| `pip install pytest`? | No: it goes to whichever Python pip belongs to and isn't recorded. uv records it in the lock file, so `uv sync` reproduces it. |

Standard dev set for every project: `uv add --dev pytest ruff`.
Kid version: flour = runtime dependency (the cake needs it) · taste-test spoon = dev dependency (only the baker needs it).
**Interview line:** "In an existing repo I use `uv init --bare`. Runtime deps (what the app imports) go in `dependencies`; tools like pytest and ruff go in the dev group, so production installs stay lean."

## Learn · pytest ✅
**Video:** [Tech With Tim: Pytest Tutorial](https://www.youtube.com/watch?v=EgpLj86ZHFQ) (0:00–30:24). Code: `drill/testing/` → **16 passed**.

| Topic | Why | How | When |
|---|---|---|---|
| Plain `assert` | prove the code gives the right answer | `assert add(2, 3) == 5` | every function with logic |
| `pytest.raises` | the error path matters as much as the happy path | `with pytest.raises(ValueError, match="..."):` | code that should refuse bad input |
| Fixture (+ `yield`) | fresh setup per test, no shared state | `@pytest.fixture`; a test asks for it by parameter name; code after `yield` = cleanup | several tests need the same object |
| `parametrize` | many cases, one test | `@pytest.mark.parametrize("num, expected", [...])` | one behaviour, many inputs |
| `tmp_path` | never touch real files | `save_totals(rows, tmp_path / "totals.csv")` | code that writes files |
| `mocker` (pytest-mock) | no real API / DB calls in tests | `mocker.patch("main.requests.get")`, `return_value`, `assert_called_once_with` | APIs, LLMs, databases |

**Mistakes I hit (and fixed):**
- Commented out the fixture → `fixture 'user_manager' not found`: a test parameter means "give me the fixture with this name"; globals don't count.
- A global object shared by tests → the second test sees the first test's data. Fixtures give each test a clean one.
- `ModuleNotFoundError: requests` even though it's mocked: the mock replaces the function after the import, so the library must be installed. `uv add requests` (no `--dev`, because my code imports it).
- `assert_called_once_with("Users.db")` failed against `"User.db"`: mock checks are exact, filename and SQL text included.

**Depth for now:** happy path + error path + mocked external call = interview-ready. Skip for now: conftest.py, fixture scopes, skip/xfail, coverage, async tests (W3).

## Still open
- PYnative OOP exercises (practice, ~1 h).
- pytest basics (next) → lab 01.
