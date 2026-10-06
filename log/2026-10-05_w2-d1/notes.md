# Mon 5 Oct 2026 · Week 2, Day 1 (finishing Week 1's topics)

## Learn · Modules, imports, venv ⏳ (in progress)
Videos, in order:
- [x] Corey: [Import Modules and Exploring the Standard Library](https://www.youtube.com/watch?v=CqvZ3vGoGs0), watched ✅. Example in `drill/modules/my_module.py` + `intro.py` (3 import styles, `sys.path`, stdlib: random, math, datetime, calendar, os)
  - `sys.path[0]` = the folder of the script you ran. `mm is my_module` → `True`, and "Imported my_module..." prints once (cached).
  - Found a stray `...\campusx\src` entry in the global `sys.path` (from an old project install): another reason to use a venv per project.
- [x] Corey: [if \_\_name\_\_ == '\_\_main\_\_'](https://www.youtube.com/watch?v=sugvnHA7ElY), watched + coded ✅
- [x] Python Morsels: [Modules are cached](https://www.youtube.com/watch?v=W9hisiG0Vq8): notes only (no code needed; `intro.py` already shows it)
- [x] chinamatt: [Relative & absolute imports](https://www.youtube.com/watch?v=nk7UWUKlfGM): watched, still unclear → relearning with the 3 videos below (old `relative_imports/` folder deleted)
- [x] Caleb Curry: [Sys.path and Changing Module Paths](https://www.youtube.com/watch?v=5z5nALNandM) (4 min) → `drill/modules/imports/syspath/where_am_i.py` (exercise TODOs)
  - `sys.path` = the list of folders searched on import, in order; `[0]` = the folder of the script you ran.
  - `sys.path.append("folder")` works but hard-codes a path → breaks on another machine / in Docker. Real fix: `python -m pkg.module` or `pip install -e .`.
  - `sys.ps1` = the `>>>` prompt in the interactive shell (trivia).
- [ ] NeuralNine: [Importing Your Own Python Modules Properly](https://www.youtube.com/watch?v=GxCXiSkm6no) (10 min) → `drill/modules/imports/own_modules/`

**Skipped (one-liners are enough for interviews):**
- **`from x import *`**: never use it. You can't tell where names came from, and it can silently overwrite your own names.
- **Circular imports**: A imports B and B imports A → `ImportError: cannot import name ...`. Fix: move the shared code into a third module.
- **`__init__.py`**: marks a folder as a package (can be empty). It runs once, on the first import from that package.
- [x] venv + uv: already known, videos skipped. Gaps filled:
  - `uv add` / `uv remove` = change the list (`pyproject.toml` + `uv.lock`). **`uv sync` = make `.venv` match `uv.lock`** (install missing, remove extra). It doesn't change the list. Run it after clone/pull.
  - `uv run python main.py` / `uv run pytest`: runs in the project venv without activating (syncs first).
  - `uv add --dev pytest ruff`: dev-only tools.
  - Commit `pyproject.toml` + `uv.lock`, never `.venv/`.
  - Plain pip still expected: `python -m venv .venv` → activate → `pip install -r requirements.txt` / `pip freeze > requirements.txt`.
- [ ] Recall: 5-min blurt + 3 quick-check questions

**How to study this:** Concept (no maths). Code along, break it on purpose (rename a module, make a `random.py`), explain "how does Python find a module?" in 60 seconds.

### `__name__` (learned)
- Run directly → `__name__ == "__main__"`. Imported → `__name__` is the module name (`"first_module"`).
- Top-level code runs on import too; only the `if __name__ == "__main__":` block is skipped.
- Pattern: put the work in `main()`, call it under the guard.
- Why logs showed `__main__`: `getLogger(__name__)` in the file you ran directly.

### Modules are cached (learned)
**One line:** a module's code runs **once**, on the first import; every later import gets the **same object** back from memory.

1. First `import my_module` → Python runs the file top to bottom and stores the result in `sys.modules["my_module"]`.
2. Every later import (same file or any other file) → finds it in `sys.modules` and returns it. **The code is not run again.**
3. Proof from `intro.py`: three imports, "Imported my_module..." printed **once**, and `mm is my_module` → `True`.

**Why it matters:**
- Module-level setup (`log = logging.getLogger(__name__)`, loading config, connecting a client) happens **once**, which is cheap.
- All importers **share** the same module, so changing a module-level variable in one file changes it for everyone.
- Editing a `.py` file while a program (or notebook) is running does nothing until you restart, or use `importlib.reload(module)`. Classic notebook confusion.
- `__pycache__/*.pyc` is a different cache: compiled bytecode on **disk**, so the next run starts faster. `sys.modules` is in **memory** during one run.

**Interview answer:** "Python executes a module once per process and caches it in `sys.modules`; later imports return the cached object. So module-level code is one-time setup and state is shared between importers."

### Absolute vs relative imports (learned)
| | Absolute | Relative |
|---|---|---|
| Looks like | `from mypackage.helpers import greet` | `from .helpers import greet` (`.` = this package, `..` = parent) |
| Works in | any file | **only inside a package** |
| Use | ✅ default (PEP 8 prefers it: clear from anywhere) | OK inside big packages to avoid long paths |

**The 3 runs in `relative_imports/`:**
- `python main.py` → ✅ works (main.py's folder is on `sys.path`, so `mypackage` is found).
- `python mypackage/core.py` → ❌ `sys.path[0]` is now `mypackage/` itself, so `mypackage` can't be found, and a relative import has no parent package.
- `python -m mypackage.core` → ✅ `-m` runs it **as part of the package**, from the parent folder.

**Rule:** files inside a package are imported, not run directly. To run one, use `python -m package.module`.

**The video's version** (`relative_imports/package/` + `setup.py`):
- `python package/moduleA.py` → ❌ `No module named 'package'`
- `python -m package.moduleA` → ✅
- **`pip install -e .`** (with `setup.py`: `setup(name="myproject", packages=find_packages())`) installs your own project in **editable** mode. Python can then import `package` from **any folder**, even with plain `python package/moduleA.py`. Edits to the code apply straight away (no reinstall).
- Done inside a venv (`relative_imports/.venv`) so the global Python stays clean.
- Modern equivalent: a `pyproject.toml` instead of `setup.py`, with the same `pip install -e .`. Lab 01 uses this.

### Gotcha: Git Bash paths
- `python D:\portfolio\...\second_module.py` in Git Bash → `can't open file 'D:\portfoliolearning-labdrill...'`: bash treats `\` as an escape and drops it.
- Fix: forward slashes (`python drill/modules/second_module.py`) or quote the path. In Git Bash, always `/`.

## Drill · logging step 5 ⏳
- `mathutils.py` ✅. `main.py` still imports `drill.logging.mathutils` → `ModuleNotFoundError` (the script's folder is on `sys.path`, not the repo root). Fix: `from mathutils import divide` + format with `%(name)s`.
