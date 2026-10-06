# W2 · D1–D2 Interview Questions · Modules · Imports · Environments

How to use: read the question, **say your answer out loud**, then open the callout. Mark ✅ / ½ / ❌ in the score table. Redo the ❌ ones tomorrow.

Levels: 🟢 screening call · 🟡 technical round · 🔴 follow-up probe

---

> [!question]- Q1 🟢 What's the difference between a module and a package?
> A module is one `.py` file. A package is a folder of modules, usually with an `__init__.py` (which can be empty). You import a package's modules with a dotted path: `from mypackage.module1 import add`.

> [!question]- Q2 🟡 How does Python find a module when you `import` it?
> It searches the folders in `sys.path`, in order: first the folder of the script you ran, then the standard library, then `site-packages` (where pip/uv install packages). The first match wins, so a local file called `random.py` shadows the real `random` module.

> [!question]- Q3 🟢 What does `if __name__ == "__main__":` do?
> When a file is run directly, its `__name__` is `"__main__"`; when it's imported, `__name__` is the module name. So the block runs only when you start that file, never when another file imports it. Put the program's entry code there, usually a `main()` call.

> [!question]- Q4 🟡 Absolute vs relative imports: which do you use?
> Absolute by default (`from mypackage.module1 import add`): explicit, readable from any file, recommended by PEP 8. Relative imports (`from .module1 import add`) only work inside a package and are fine for imports within one package. They fail in a script you run directly.

> [!question]- Q5 🟡 You get `ModuleNotFoundError` for your own package. How do you fix it?
> Check where you ran from: `sys.path[0]` is the script's folder, so a file inside the package can't see the package itself. Fixes: run from the project root with `python -m package.module`, or install the project with `pip install -e .` (or `uv sync`). Avoid `sys.path.append`: it hard-codes a path that breaks on other machines.

> [!question]- Q6 🟡 What does `pip install -e .` do?
> Installs your own project (from `pyproject.toml` in the current folder) in editable mode: a link to your source, not a copy. Your package becomes importable from anywhere (tests, notebooks) and code changes apply without reinstalling.

> [!question]- Q7 🟡 What's the difference between `pyproject.toml` and a lock file like `uv.lock`?
> `pyproject.toml` declares what the project needs, usually as version ranges, plus project metadata. The lock file pins the exact resolved versions of every package, including dependencies of dependencies, so every machine installs the identical set. `uv sync` applies the lock.

> [!question]- Q8 🟢 Why don't you commit the `.venv` folder?
> It's machine-specific: it contains paths and compiled files for this OS and Python version, so it breaks on another machine or in Docker. It's also rebuildable: `uv sync` (or `pip install -r requirements.txt`) recreates it from the lock file.

> [!question]- Q9 🔴 Why avoid `from x import *` and what causes circular imports?
> `import *` hides where names come from and can silently overwrite your own names. A circular import is A importing B while B imports A, giving `ImportError: cannot import name ...`. The fix is to move the shared code into a third module both can import.

---

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Attempt 1 | | | | | | | | | |
| Attempt 2 | | | | | | | | | |
