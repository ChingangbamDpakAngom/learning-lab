# What I've learned, in order

My learning record for interview preparation: every topic in the order I learned it, the resources I actually used, and where my code and notes are.
Revise a topic with the [Topic Cards](https://claude.ai/artifact/FQhbAeERhqnSYSBS7UgVpK); find more resources in the [Roadmap Library](https://claude.ai/artifact/DpMiXAhi6wVtuU1A6qJ8Nt).

**How I learn each topic:** watch or read the listed sections (not whole courses) → code along in `drill/` → recall out loud (what · why · how · solves · when) → cheat sheet + interview questions → topic card.
"Learned in chat" = taught step by step in the learning chat, no external video.

---

## Week 0 · Setup (25–27 Sep 2026)

### 1. Big-O, two pointers, descriptive statistics · 25 Sep
- **Resources:** learned in chat.
- **Practice:** NumPy drill: 1,000 random numbers → mean, median, SD, histogram.
- **Notes:** [notes](../log/2026-09-25_w0-d1/notes.md) · cheat sheets: [Big-O](../log/2026-09-25_w0-d1/Big-O-Cheat-Sheet.jpg) · [Two pointers](../log/2026-09-25_w0-d1/Two-Pointers-Cheat-Sheet.jpg) · [Descriptive stats](../log/2026-09-25_w0-d1/Descriptive-Statistics-Cheat-Sheet.jpg) · [Interview Qs](../log/2026-09-25_w0-d1/Interview-Questions.md)
- **Key idea:** Big-O = how work grows with input size; median beats mean on skewed data.

### 2. Docker + Redis basics · 25 Sep
- **Resources:** learned in chat (for the Aegis project).
- **Notes:** [notes](../log/2026-09-25_w0-d1/notes.md) · [Docker Qs](../log/2026-09-25_w0-d1/docker-questions.md)
- **Key idea:** an image runs the same everywhere; Redis = in-memory cache with a TTL.

---

## Week 1 · Python core, errors, logging (28 Sep – 4 Oct)

### 3. Python core: functions, data structures, comprehensions · 28 Sep
- **Resources:** learned in chat. Reference: [The Python Tutorial](https://docs.python.org/3/tutorial/) ch. 4–5.
- **Notes:** [notes](../log/2026-09-28_w1-d1/notes.md) · [Python core cheat sheet](../log/2026-09-28_w1-d1/Python-Core-Cheat-Sheet.jpg) · quiz 5/7
- **Key idea:** set/dict lookup is O(1), list is O(n); pick the container by what you need to do fast.

### 4. Error handling, file I/O, retries · 2 Oct
- **Resources:** learned in chat (quick check 3/3).
- **Notes:** [notes](../log/2026-10-02_w1-d5/notes.md) · [cheat sheet](../log/2026-10-02_w1-d5/Error-Handling-File-IO-Cheat-Sheet.jpg) · [Interview Qs](../log/2026-10-02_w1-d5/Interview-Questions.md)
- **Key idea:** catch narrow errors; `with` closes files; retry only temporary failures (timeouts, 5xx, 429).

### 5. Logging · 3 Oct
- **Resources:** Corey Schafer [Logging Basics](https://www.youtube.com/watch?v=-ARI4Cz-awo) (whole) · [Logging Advanced](https://www.youtube.com/watch?v=jxmzY9soFXg) (first ~10 min).
- **Code:** [`drill/logging/`](../drill/logging/) (practice.py, mathutils.py, main.py)
- **Notes:** [notes](../log/2026-10-03_w1-d6/notes.md) · [cheat sheet](../log/2026-10-03_w1-d6/Logging-Cheat-Sheet.jpg) · [Interview Qs](../log/2026-10-03_w1-d6/Interview-Questions.md)
- **Key idea:** `getLogger(__name__)` in every module; `basicConfig` once in main; `log.exception` inside `except`.

---

## Week 2 · Python foundations (5–11 Oct)

### 6. Modules, imports, `__name__`, sys.path · 5–6 Oct
- **Resources:**
  - Corey Schafer [Import Modules and Exploring the Standard Library](https://www.youtube.com/watch?v=CqvZ3vGoGs0)
  - Corey Schafer [if \_\_name\_\_ == '\_\_main\_\_'](https://www.youtube.com/watch?v=sugvnHA7ElY)
  - Python Morsels [Modules are cached](https://www.youtube.com/watch?v=W9hisiG0Vq8)
  - chinamatt [Relative & absolute imports](https://www.youtube.com/watch?v=nk7UWUKlfGM)
  - Caleb Curry [Sys.path and Changing Module Paths](https://www.youtube.com/watch?v=5z5nALNandM)
  - NeuralNine [Importing Your Own Python Modules Properly](https://www.youtube.com/watch?v=GxCXiSkm6no)
- **Code:** [`drill/modules/`](../drill/modules/)
- **Notes:** [5 Oct](../log/2026-10-05_w2-d1/notes.md) · [6 Oct](../log/2026-10-06_w2-d2/notes.md) · [cheat sheet](../log/2026-10-06_w2-d2/Modules-Imports-Cheat-Sheet.jpg) · [Interview Qs](../log/2026-10-06_w2-d2/Interview-Questions.md)
- **Key idea:** imports search `sys.path` in order (script folder first); absolute imports by default.

### 7. `python -m`, `pip install -e .`, venv + uv · 6 Oct
- **Resources:** anthonywritescode [don't run `python my/script.py`!](https://www.youtube.com/watch?v=hgCVIa5qQhM) · [setuptools: Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) (first section) · venv/uv: already known.
- **Notes:** [6 Oct](../log/2026-10-06_w2-d2/notes.md)
- **Key idea:** `-m` = run it properly, `-e` = install it properly; commit `pyproject.toml` + `uv.lock`, never `.venv`.

### 8. OOP: classes, class variables, class/static methods, inheritance, @property, the 4 pillars · 7 Oct
- **Resources:**
  - Corey Schafer [OOP 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
  - Corey Schafer [OOP 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho)
  - Corey Schafer [OOP 3: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
  - Corey Schafer [OOP 4: Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE)
  - Corey Schafer [OOP 6: Property Decorators](https://www.youtube.com/watch?v=jCzT9XFZ5bw)
  - OOP 5 (dunder methods) skipped: only `__repr__` vs `__str__`, learned in chat.
  - Abstraction (ABC) and polymorphism: learned in chat.
- **Code:** [`drill/oop/`](../drill/oop/) (oop1 → oop6)
- **Notes:** [OOP cheat sheet](../log/2026-10-06_w2-d2/OOP-Cheat-Sheet.jpg) · [29 OOP interview Qs](../log/2026-10-06_w2-d2/OOP-Interview-Questions.md)
- **Practice still to do:** [PYnative OOP exercises](https://pynative.com/python-object-oriented-programming-oop-exercise/)
- **Key idea:** `self` = the object the method was called on; encapsulation, abstraction, inheritance, polymorphism.

### 9. Dataclasses (and dataclass vs Pydantic) · 8 Oct
- **Resources:** ArjanCodes [This Is Why Python Data Classes Are Awesome](https://www.youtube.com/watch?v=CvQ7e6yUtnw) (0:00–15:00) · [dataclasses docs](https://docs.python.org/3/library/dataclasses.html)
- **Code:** [`drill/oop/dataclasses_basics.py`](../drill/oop/dataclasses_basics.py)
- **Notes:** [8 Oct](../log/2026-10-08_w2-d4/notes.md)
- **Key idea:** dataclass writes `__init__`/`__repr__`/`__eq__`; Pydantic validates untrusted data at the boundaries.

### 10. uv setup + dev dependencies · 8 Oct
- **Resources:** learned in chat.
- **Notes:** [8 Oct](../log/2026-10-08_w2-d4/notes.md)
- **Key idea:** `uv init --bare` for an existing repo; `--dev` only for tools my code doesn't import (pytest, ruff).

### 11. pytest: assert, raises, fixtures, parametrize, tmp_path, mocking · 8 Oct
- **Resources:** Tech With Tim [Pytest Tutorial](https://www.youtube.com/watch?v=EgpLj86ZHFQ) (0:00–30:24) · [pytest tmp_path docs](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- **Code:** [`drill/testing/`](../drill/testing/) → 16 tests passing
- **Notes:** [8 Oct](../log/2026-10-08_w2-d4/notes.md) · **[explainer: raises, parametrize, mocker](explainers/pytest-raises-parametrize-mocker.md)**
- **Key idea:** test the happy path, the error path, and external calls (mocked).

---

## Next
Lab 01 (NHSBSA downloader + tests) · NumPy + pandas · SQL joins/CTEs/windows · git + argparse.
