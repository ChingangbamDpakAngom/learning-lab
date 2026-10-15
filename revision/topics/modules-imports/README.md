# Modules, imports, environments (venv, uv, `-m`, `-e`)

**Status:** ✅ done · **Sessions:** [5 Oct](../../../log/2026-10-05_w2-d1/notes.md) · [6 Oct](../../../log/2026-10-06_w2-d2/notes.md) · [8 Oct, uv setup](../../../log/2026-10-08_w2-d4/notes.md) · **Code:** [`drill/modules/`](../../../drill/modules)
**Cheat sheet:** [Modules + imports](Modules-Imports-Cheat-Sheet.jpg) · **Interview Qs:** [6 Oct set](Interview-Questions.md) · [short answers](../../INTERVIEW-QA.md#modules-imports--environments)
**Resources:** Corey Schafer *Import Modules* + *`if __name__ == '__main__'`* · Python Morsels *Modules are cached* · Caleb Curry *sys.path* · NeuralNine *Importing Your Own Modules* · anthonywritescode *don't run `python my/script.py`*

## Must know
- **How import finds things:** `sys.path` in order (script folder → stdlib → site-packages), first match wins.
- `__name__` is `"__main__"` when run, the module name when imported. Put the work in `main()` under the guard.
- **Modules are cached:** code runs once per process, stored in `sys.modules`; later imports get the same object. So module-level setup runs once and state is shared. `__pycache__` = bytecode on disk, a different cache.
- **Absolute by default** (`from mypackage.helpers import greet`); relative (`from .helpers import greet`) only inside a package, never in a script run directly.
- `__init__.py` marks a package and can re-export (`from .module1 import add`) for short imports.
- Files inside a package are imported, not run. To run one: `python -m package.module` from the project root.
- `pip install -e .` = **editable** install: a link to my source, importable from anywhere, edits apply without reinstall.
- `python -m pip install x` = the pip of *this* Python.
- `sys.path.append(...)` works but hard-codes a path → breaks elsewhere. Real fix: `-m` or `-e`.
- Skip-level one-liners: never `from x import *`; circular import → move shared code to a third module.

**Environments**
- venv per project, always. `pyproject.toml` = what I asked for (ranges); `uv.lock` = exact versions of everything. Commit both, never `.venv` (machine-specific + rebuildable).
- `uv add` / `uv remove` change the list; `uv sync` makes `.venv` match the lock (after clone/pull). `uv run` = no activation.
- Existing repo → `uv init --bare`. Runtime deps (my code imports it) → `uv add`; tools (pytest, ruff) → `uv add --dev`.
- Plain pip still expected: `python -m venv .venv` → `pip install -r requirements.txt`.

## Mistakes I made
- Said "absolute vs relative" for how import finds modules (it's `sys.path` order).
- Called `-e` "executable" (it's **editable**).
- Gave a vague reason for not committing `.venv`.
- Git Bash: backslash paths get eaten → always use `/`.

## Gaps
- [ ] None open on theory. Use `-m` and `uv sync` for real in lab 01.
