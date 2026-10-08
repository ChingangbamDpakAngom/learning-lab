# Interview Q&A: short answers

Theory only, separate from the practical lessons in `log/`. Answer out loud first, then check. Answers are interview-length: 1–3 sentences.
Levels: 🟢 screening · 🟡 technical · 🔴 follow-up probe. Last updated: 8 Oct 2026.

## Big-O
- 🟢 **What does Big-O tell you?** How time or memory grows as input size n grows (usually worst case). Constants are dropped because they don't change how cost scales.
- 🟢 **Time and space of a set-based duplicate check?** O(n) time (one pass, O(1) set lookups) and O(n) space (the set). Always say both.
- 🟡 **Nested loop `for i in range(n): for j in range(i, n)`?** O(n²): it runs n(n+1)/2 times.
- 🟢 **Loop that halves `i` each step?** O(log n).
- 🟡 **Loop over list a, inner loop over list b?** O(a·b), two separate inputs. Only O(n²) if they're the same size.
- 🟡 **Hidden cost in `if x in b_list` inside a loop?** `in` on a list is O(m), so O(n·m). Convert to a set once → O(n + m) time, O(m) space.
- 🟡 **Why is `append` O(1) when lists resize?** Amortised O(1): resizes grow proportionally, so the rare O(n) copies average out.
- 🟡 **Three O(n) operations that look cheap?** `x in list`, `list.pop(0)` / `insert(0, x)`, slicing, string `+` in a loop. Use `deque.popleft()` for queues.
- 🔴 **Is dict lookup always O(1)?** Average O(1); worst case O(n) when keys collide.
- 🟡 **How do you improve an O(n²) solution?** Replace an inner search with a hash map (O(n)), sort then two pointers / binary search (O(n log n)), or use a sliding window (O(n)). State the space trade-off.
- 🟢 **Space of `s[::-1]` and of recursion depth d?** O(n) for the copy; O(d) call-stack frames.

## Two pointers
- 🟢 **When do you use two pointers?** Sorted array + pair/triplet sum, palindromes, in-place removal, merging sorted lists.
- 🟡 **Why does sorted Two Sum with two pointers never miss?** Too big → the right value can't pair with anything, drop it; too small → drop the left. Each step safely removes one element: O(n).
- 🟡 **Unsorted Two Sum returning indices: two pointers or hash map?** Hash map, O(n) time and space. Sorting costs O(n log n) and loses the indices.
- 🟡 **Container With Most Water: why move the shorter line?** Area is capped by the shorter line, so moving the taller one can only shrink the area.
- 🟡 **3Sum approach?** Sort, fix an anchor, run Two Sum II on the rest: O(n²). Skip equal anchors and equal values after a hit to avoid duplicates.
- 🟢 **`l < r` or `l <= r`?** `l < r` for pairs (two different elements); `l <= r` for binary search.

## Descriptive statistics
- 🟢 **Mean or median for UK salaries?** Median: salaries are right-skewed and the median is robust to outliers.
- 🟢 **Mean > median means?** Right skew: a long tail of high values (income, house prices, latency).
- 🟡 **Why square deviations?** Raw deviations sum to zero; squaring makes them positive and penalises big ones (that's why MSE is a standard loss).
- 🟡 **Why divide by n − 1 for a sample?** The sample mean sits closer to its own points, so dividing by n underestimates variance; n − 1 (Bessel's correction) fixes the bias.
- 🔴 **`np.var` vs `pd.Series.var` differ. Why?** NumPy defaults to ddof=0 (population), pandas to ddof=1 (sample). Set `ddof` explicitly.
- 🟢 **Why report SD instead of variance?** SD is in the data's units; variance is in squared units.
- 🟡 **How do you detect outliers in skewed data?** IQR rule (below Q1 − 1.5·IQR or above Q3 + 1.5·IQR): it's robust. z-score |z| > 3 assumes roughly normal data.
- 🟢 **What is a z-score?** (x − mean) / SD: how many SDs from the mean.
- 🟢 **68–95–99.7 rule?** For normal data, ~68% within ±1 SD, 95% within ±2, 99.7% within ±3. Not for skewed data.
- 🟡 **Why monitor p95/p99 latency, not the mean?** Latency is right-skewed; the mean hides the slow tail users actually feel.
- 🟡 **Why standardise features, and the classic mistake?** Distance-based models and gradient descent need comparable scales. Mistake: fitting the scaler on all data (leakage); fit on train only, or use a Pipeline.

## Python core
- 🟢 **List vs tuple?** List is mutable; tuple is immutable, so it's hashable and can be a dict key or set member. Use a tuple for fixed records.
- 🟡 **What's wrong with `def add(item, items=[])`?** The default list is created once when `def` runs and is shared across calls. Use `items=None`, then `items = []` inside.
- 🟢 **Does `b = a` copy a list?** No: both names point to the same list. Use `a.copy()` (shallow) or `copy.deepcopy` (nested).
- 🟢 **Why can't a list be a dict key?** Keys must be hashable; mutable built-ins aren't.
- 🟡 **50k codes, 1M membership checks: list or set?** Set: O(1) average per check vs O(n) for a list (5·10¹⁰ steps).
- 🟢 **What's falsy in Python?** `0`, `""`, `[]`, `{}`, `None`, `False`. `if n % 2` means "n is odd".
- 🟢 **List comprehension vs generator expression?** `[...]` builds the whole list in memory; `(...)` is lazy, one item at a time, for big data.

## Errors + file I/O
- 🟢 **Why is `except Exception: pass` bad?** It hides real bugs and the traceback. Catch the narrowest exception you can handle.
- 🟢 **`else` vs `finally`?** `else` runs only if nothing was raised; `finally` always runs (cleanup).
- 🟢 **What does `with open(...)` guarantee?** The file is closed even if an exception is raised.
- 🟡 **`raise X from e`?** Raises a clearer error and chains the original as its cause, so both tracebacks show.
- 🟡 **When write a custom exception?** When callers must handle your errors differently from bugs, e.g. `DownloadError` → friendly message, bugs still crash.
- 🟡 **Which API errors do you retry?** Transient only: timeouts, 5xx, 429 (honour `Retry-After`). Never 400/401/404. Exponential backoff, capped attempts, a timeout on every request.
- 🟡 **Why `encoding="utf-8"` and `newline=""` for CSV?** Windows' default encoding breaks non-ASCII; `newline=""` stops blank rows on Windows.
- 🔴 **Idempotent download job?** Running it twice = running it once (skip existing files or overwrite atomically, never append duplicates), so retries are safe.

## Logging
- 🟢 **Logging vs print?** Levels you can switch, timestamps, source module, and output to files or monitoring tools.
- 🟢 **Levels in order and the default?** DEBUG < INFO < WARNING < ERROR < CRITICAL; default WARNING.
- 🟡 **Why `getLogger(__name__)`?** Each module gets a named logger: you see who logged and can set levels per module.
- 🟡 **Where do you configure logging?** Once, in `main`. `basicConfig` only works on the first call, so libraries must never call it.
- 🟡 **`log.exception`?** Logs at ERROR with the full traceback; use it inside `except`.
- 🟡 **`log.info("rows=%s", n)` vs an f-string?** The message is only built if the level is on, and the template stays constant for log search.
- 🔴 **Structured logs and request IDs?** JSON fields instead of free text so logs can be filtered; a request ID on every line lets you follow one request across services.

## Modules, imports + environments
- 🟢 **Module vs package?** A module is one `.py` file; a package is a folder of modules (usually with `__init__.py`).
- 🟡 **How does Python find a module?** It searches `sys.path` in order: the script's folder, the standard library, site-packages. First match wins (a local `random.py` shadows the real one).
- 🟢 **`if __name__ == "__main__":`?** Runs only when the file is executed directly, not when imported.
- 🟡 **Why does a module's code run only once?** It's cached in `sys.modules` after the first import; later imports get the same object.
- 🟡 **Absolute vs relative imports?** Absolute by default (clear from anywhere, PEP 8). Relative (`.`) only inside a package.
- 🟡 **Fix `ModuleNotFoundError` for your own package?** Run from the project root with `python -m pkg.module`, or install it with `pip install -e .`. Avoid `sys.path.append`.
- 🟡 **`python -m` vs `pip install -e .`?** `-m` runs a module by name with the current folder on the path; `-e` installs your project in editable mode so it imports from anywhere.
- 🟡 **`pyproject.toml` vs `uv.lock`?** pyproject declares what you need (ranges); the lock pins exact versions of everything so every machine matches.
- 🟢 **Why not commit `.venv`?** Machine-specific and rebuildable from the lock (`uv sync`).
- 🔴 **`import *` and circular imports?** `import *` hides where names come from; circular imports (A↔B) are fixed by moving shared code to a third module.

## OOP
- 🟢 **Class vs instance?** Class = blueprint; instance = one object built from it, with its own data.
- 🟢 **What is `self`?** The instance the method was called on (`emp.fullname()` = `Employee.fullname(emp)`).
- 🔴 **Is `self` a keyword?** No, just a convention for the first parameter.
- 🟡 **Is `__init__` the constructor?** Strictly no: `__new__` creates the object, `__init__` initialises it.
- 🔴 **Two objects with equal values: is `a == b` True?** Not by default (identity). Define `__eq__` or use `@dataclass`.
- 🟢 **Instance vs class variable?** Instance: `self.x`, one per object. Class: in the class body, shared.
- 🔴 **`emp_1.raise_amount = 1.05` changes what?** Only emp_1: it creates an instance variable that shadows the class one.
- 🟢 **Normal method vs classmethod vs staticmethod?** Needs the object → normal (`self`); needs the class (shared values, alternative constructors) → `@classmethod` (`cls`); needs neither → `@staticmethod`.
- 🟡 **Why return `cls(...)` in an alternative constructor?** So subclasses get their own type back.
- 🟢 **What does `super().__init__()` do?** Reuses the parent's setup instead of rewriting it.
- 🟡 **Method resolution order?** Instance → child → parent; first match wins, so children override.
- 🟡 **`__str__` vs `__repr__`?** `__str__` is readable for users; `__repr__` is unambiguous for developers. If only one, write `__repr__`.
- 🟢 **The 4 pillars?** Encapsulation (bundle + control access), abstraction (hide details, ABC contracts), inheritance (reuse), polymorphism (same call, different behaviour).
- 🟡 **Why `@property`?** It recomputes on every read (mirror, not photo) while callers use attribute syntax; setters can validate.
- 🔴 **Private attributes in Python?** None truly private: `_x` is convention, `__x` is name-mangled but reachable.
- 🟡 **Why can't you instantiate a class with an `@abstractmethod`?** It only promises the method; subclasses must implement it first.

## Dataclasses
- 🟢 **What does `@dataclass` generate?** `__init__`, `__repr__` and `__eq__` (value comparison) from type-hinted fields.
- 🟡 **Why `field(default_factory=list)`?** `= []` would be shared by all objects; the factory makes a fresh list each time.
- 🟡 **What is `__post_init__` for?** It runs after the generated `__init__` to compute or validate fields (e.g. reject negative pay).
- 🟡 **`frozen=True` and its gotcha?** Read-only and hashable; it also blocks assignments in your own `__post_init__`.
- 🔴 **Dataclass or Pydantic for an API request body?** Pydantic: it validates and converts untrusted input (FastAPI returns 422). Dataclass type hints aren't checked.

## Docker
- 🟢 **Image vs container?** Image = read-only template built in layers; container = a running instance with a writable layer.
- 🟢 **Why Docker for ML?** Reproducible environments, easy deployment, isolation, fast start.
- 🟡 **Container vs VM?** VMs run a full guest OS; containers share the host kernel, so they're lighter and faster with weaker isolation.
- 🟡 **Why copy `requirements.txt` before the code?** Layer caching: dependencies change rarely, so that slow layer stays cached.
- 🟡 **App in a container doesn't answer on localhost?** Missing `-p 8000:8000`, or the app binds to 127.0.0.1 instead of 0.0.0.0.
- 🟡 **Data gone after restart?** The writable layer is temporary; use a named volume.
- 🟡 **Compose service can't reach `localhost:6379`?** Use the service name (`redis:6379`); `depends_on` doesn't wait for readiness.
- 🟢 **`RUN` vs `CMD`?** `RUN` executes at build time; `CMD` is the default command at start.

## Redis
- 🟢 **What is Redis and why fast?** In-memory data-structure store; RAM, simple operations, single-threaded command execution.
- 🟡 **Cache-aside?** Read: cache hit → return; miss → DB, then `SET` with a TTL. Write: update DB, delete the key. Watch stale data and stampedes.
- 🟡 **TTL vs eviction?** TTL is a lifetime you set; eviction is Redis freeing memory when full (`allkeys-lru`).
- 🔴 **Lost update with GET + SET?** Race condition; use atomic `INCR` (or MULTI/EXEC, Lua).
- 🟡 **Redis vs Postgres for everything?** RAM is costly, durability weaker, no rich queries: Redis sits beside the database.

## Coming next (added as I learn them)
pytest · argparse · git · NumPy · pandas · SQL joins/CTEs/windows · generators, decorators, `*args/**kwargs`, the GIL · then W3 (async, FastAPI, LLM basics, prompting, structured output, tool calling).
