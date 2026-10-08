# Tue 6 Oct 2026 · Week 2, Day 2 (modules lesson, continued)

**Revision:** [Modules + Imports cheat sheet](Modules-Imports-Cheat-Sheet.jpg) · [9 interview questions](Interview-Questions.md) (covers W2 D1 + D2) · [OOP cheat sheet](OOP-Cheat-Sheet.jpg) · [29 OOP questions](OOP-Interview-Questions.md)

## Key points: why · how · when (revise from this table)
**Study strategy:** remember *why it exists, how it works, when to use it*, not every line of code. Exception: a few core lines to type from memory for live coding:
```python
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
from mypackage.module1 import add
```

| Topic | Why it exists | How (the idea) | When to use it |
|---|---|---|---|
| **Logging** | `print` can't be switched off, has no timestamp, doesn't say which file wrote it | each module gets a named logger; only `main` configures, once | any code that runs unattended: pipelines, APIs, jobs |
| **Log levels** | not every message matters equally | DEBUG < INFO < WARNING < ERROR; you see your level and above | INFO milestones · WARNING retries · ERROR failures |
| **`log.exception`** | a failure without a traceback is hard to debug | inside `except`: logs the error + where it happened | every `except` that handles a failure |
| **`sys.path`** | Python must know where to look for imports | list of folders searched in order; first = folder of the script you ran | on `ModuleNotFoundError`: *which folder did I run from?* |
| **`__name__`** | the same file can be run or imported | `"__main__"` when run, the module name when imported | start-up code under `if __name__ == "__main__":` |
| **Absolute vs relative imports** | code references other files in a package | absolute = full path; relative = `.` (this package) | absolute by default; relative only inside a package |
| **`__init__.py`** | Python must know a folder is a package | marks the package; can re-export names | every package; re-export for short imports |
| **Modules cached** | re-running setup on every import wastes time | runs once, stored in `sys.modules` | explains why module-level setup happens once |
| **`-m`** | files inside a package can't see the package when run directly | runs the module by name from the current folder | running a file inside a package |
| **`pip install -e .`** | your own project must be importable everywhere | installs a link to your source, not a copy | tests / notebooks importing your project |
| **venv** | projects need different package versions | each project gets its own private packages | every project, always |
| **`pyproject.toml` / `uv.lock`** | same setup on every machine | toml = what you asked for; lock = exact versions installed | commit both; never `.venv` |
| **`uv sync`** | a fresh clone has no venv | builds `.venv` to match the lock | after clone or pull |
| **`pprint`** | long data is unreadable on one line | one item per line | inspecting JSON / long lists |

**Interview pattern:** what it is → why it exists → when to use it → an example from my project.

## Learn · `-m` and `-e` ✅
**How to study this:** Concept (no maths). Explain each in one sentence, then use them for real in lab 01.

### `python -m`: run a module by its name, not its file path
```bash
python -m package.moduleA       # instead of: python package/moduleA.py
```
- Python searches from the **folder you're in**, so `package` is found and the package's own imports (absolute + relative) work.
- Rule: a file **inside a package** is run with `-m`, from the project root.
- Already used daily: `python -m venv .venv` · `python -m pip install x` (the pip of *this* Python, avoids "wrong pip" bugs) · `python -m pytest`.

### `pip install -e .`: install your own project in editable mode
- `.` = the project in this folder (reads `pyproject.toml`).
- Installs a **link** to your source folder, not a copy → importable from anywhere (tests, notebooks, other folders), and edits apply with no reinstall.
- With uv: in a packaged uv project, `uv sync` installs the project editable automatically.

| Situation | Use |
|---|---|
| Run a file inside a package | `python -m pkg.module` |
| Tests can't import my code (`ModuleNotFoundError`) | `pip install -e .` (or `uv sync`) |
| Make sure pip installs into the right Python | `python -m pip install ...` |

**Interview line:** "`-m` runs a module by name with the current folder on the path, so package imports work. `pip install -e .` installs my project in editable mode, so it's importable everywhere and changes apply without reinstalling."

**Skip:** how editable installs work internally (`.pth` files, build backends).

### `pprint`: pretty print (seen in the `-m` video)
- Prints **any long or nested data** (lists, dicts, JSON) one item per line instead of one long line. Not specific to directories: the video used it because `sys.path` is a long list.
```python
from pprint import pprint
pprint(sys.path)          # list of folders, one per line
pprint(response.json())   # nested API response
print(json.dumps(data, indent=2))   # same idea for JSON
```
- Standard library, no install. Rule: if `print()` gives one unreadable line, use `pprint()`. Debugging convenience, not an interview topic.

## Recall · answers checked
| Question | My answer | Interview-ready version |
|---|---|---|
| What does `uv sync` do? | updates the venv's installed packages to match `uv.lock` ✅ | (same) Run after clone/pull. `uv add`/`uv remove` change the list; `sync` only applies it |
| Absolute vs relative imports? | absolute for a fixed folder layout, relative if folders may move ½ | **Absolute by default** (explicit, PEP 8, editors refactor them). Relative only for imports *within one package*; it survives renaming the whole package but breaks if one file moves, and never works in a script run directly |
| `pyproject.toml` vs `uv.lock`? | toml = shopping list of what I need; lock = the exact packages in detail ✅ | toml = what you **asked for** (ranges like `requests>=2.31`) + project metadata. lock = **exact** resolved versions of everything, incl. dependencies of dependencies → identical installs everywhere |
| Why not commit `.venv/`? | sharing the blueprint beats sharing all the packages ½ → retry: it depends on the folder location, so `uv sync` builds the right one on each machine ✅ | it's **machine-specific** (paths + compiled files for this OS/Python → breaks on Mac/Linux/Docker) and **rebuildable** with `uv sync` from the lock |

## Videos left for today (~65 min)
**Modules (finish the topic)**
- [ ] anthonywritescode: [don't run `python my/script.py`!](https://www.youtube.com/watch?v=hgCVIa5qQhM) (8 min): `-m`
- [x] NeuralNine: [Importing Your Own Python Modules Properly](https://www.youtube.com/watch?v=GxCXiSkm6no) (10 min) → `drill/modules/imports/own_modules/` (example code written, runs)
  - Local file → `import mymodule` (same folder = `sys.path[0]`).
  - Package module → `from mypackage.module1 import add`; nested → `from mypackage.subpackage.submodule import shout`.
  - `__init__.py` can re-export (`from .module1 import add`) → users write the short `from mypackage import add`.
  - Professional layout: logic lives in the package (`myapp/core.py`); `main.py` is a thin entry point that imports and starts it.

| Chapter | Import | Idea |
|---|---|---|
| 2 Local file | `import mymodule` | same folder as the script → found via `sys.path[0]` |
| 3 Package | `from mypackage.module1 import add` | folder.file as a dotted path |
| 4 `__init__.py` | `from mypackage import multiply` | `__init__.py` re-exports it (`from .module2 import multiply`) → short form works |
| 5 Nested | `from mypackage.subpackage.submodule import shout` | one more dot per folder level |
| 6 Professional | `professional/main.py` → `from myapp import run` | logic in the package, thin entry point |

Run: `python main.py` from `own_modules/` → `Hello, Deepak! · 5 · 6 · IMPORTS WORK!`; `python main.py` from `professional/` → `myapp is running`.

**Experiment:** empty `mypackage/__init__.py` → the chapter-4 short import breaks, the chapter-3 full path still works. That's what `__init__.py` re-exports are for.
- `-e` has no good short video → [setuptools: Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html), first section only (3 min read)

**OOP (Week 1 carry-over, essentials only)**
- [x] Corey: [OOP 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) (15 min) → `drill/oop/oop1_classes.py` (runs). **`self` = the instance the method was called on** (`emp_1.who_am_i()` → `self is emp_1` True); `obj.method()` = `Class.method(obj)`. Chose `email()` as a method (stays correct if `first` changes). [10 OOP interview questions](OOP-Interview-Questions.md)
- [x] Corey: [OOP 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho) (12 min) → `drill/oop/oop2_class_variables.py` (runs). Class var lives in the class body, shared; `self.x` looks on instance then class; assigning via an instance shadows it; counters use `Employee.num_of_emps`. Q11–15 added to OOP questions.
- [x] Corey: [OOP 4: Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE) (20 min) → `drill/oop/oop4_inheritance.py` (runs). `super()` reuses the parent's setup; lookup instance → child → parent (MRO); `employees=None` avoids the shared-list trap. OOP 5 skipped: only `__repr__` (developer view) vs `__str__` (user view). Next: OOP 6 property + 4 pillars. Fix: indentation mixes 4/5/8/10 spaces → use 4 (Shift+Alt+F).

- [x] Corey: [OOP 6: Property Decorators](https://www.youtube.com/watch?v=jCzT9XFZ5bw) + 4 pillars → `drill/oop/oop6_property_and_pillars.py` (runs). Property = mirror not photo; `ABC` = contract; polymorphism = same `.area()`, different result. Q24–29 in OOP questions. **OOP topic complete.** Practice: [PYnative OOP exercises](https://pynative.com/python-object-oriented-programming-oop-exercise/); later LeetCode design problems (Min Stack, LRU Cache).

**Skipped (one-liners instead):**
- ✅ OOP 3 done after all (classic interview question) → `drill/oop/oop3_class_static_methods.py` (runs). Normal method = about **me** (`self`), `@classmethod` = about **our school** (`cls`: shared values, alternative constructors like `from_string`), `@staticmethod` = about **neither** (`is_workday`). Bugs fixed: `day.weekday` without `()`, `pay` left as a string, `import datetime` inside the class (belongs at file top). Q16–18 in OOP questions.
- OOP 5: dunder methods like `__repr__` / `__len__` customise built-in behaviour (`print`, `len`).
- OOP 6: `@property` lets a method be read like an attribute.


## Still open
- ✅ Modules recall blurt: 2/5 first try → retry Q1 + Q4 ✅. Weak spots fixed:
  - Q1 how import finds things = **`sys.path` in order** (script folder → stdlib → site-packages), first match wins. *Not* "absolute vs relative" (that's import style).
  - Q4 `-m` = **run** a module by name from the root (package imports work); `-e` = **editable** install (not "executable"): my project imports from anywhere.
  - Q5 `uv.lock` is the blueprint; `.venv` is the built result → machine-specific + rebuildable, so never committed.
- ✅ Logging drill step 5 done: `from mathutils import divide`; log lines now show **`mathutils`** (the module that logged), not `__main__`. Lesson: Python runs what's **saved on disk**, so check with `sed -n 8p file` when an edit "doesn't work".
- Not videos: dataclasses (docs, 10 min) and pytest (docs, 30 min) before lab 01. NumPy → tomorrow.
