# OOP + dataclasses

**Status:** ✅ done · **Sessions:** [6–7 Oct](../../log/2026-10-06_w2-d2/notes.md) · [8 Oct, dataclasses](../../log/2026-10-08_w2-d4/notes.md) · **Code:** [`drill/oop/`](../../drill/oop/) (oop1 → oop6, dataclasses_basics.py)
**Cheat sheet:** [OOP](../../log/2026-10-06_w2-d2/OOP-Cheat-Sheet.jpg) · **Interview Qs:** [29 OOP Qs](../../log/2026-10-06_w2-d2/OOP-Interview-Questions.md) · [dataclass Qs (8 Oct)](../../log/2026-10-08_w2-d4/notes.md#interview-questions) · short answers: [OOP](../INTERVIEW-QA.md#oop), [Dataclasses](../INTERVIEW-QA.md#dataclasses)
**Resources:** Corey Schafer OOP 1, 2, 3, 4, 6 · ArjanCodes *Data Classes* (0:00–15:00)

## Must know
**Classes**
- `self` = the instance the method was called on; `obj.method()` = `Class.method(obj)`.
- Class variable: in the class body, shared. `self.x` looks on the instance, then the class; assigning via an instance shadows it. Counters use `Employee.num_of_emps`.
- Normal method = about **me** (`self`) · `@classmethod` = about **the class** (`cls`: alternative constructors like `from_string`) · `@staticmethod` = about **neither** (`is_workday`).
- Inheritance: `super().__init__(...)` reuses the parent's setup; lookup goes instance → child → parent (MRO). `employees=None`, not `[]`.
- `@property`: a method read like an attribute; always up to date ("mirror, not photo"). Setter/deleter for controlled changes.
- `__repr__` = developer view, `__str__` = user view. Dunders customise built-ins (`len`, `print`).
- **4 pillars:** encapsulation (hide state behind methods) · abstraction (`ABC` + `@abstractmethod` = a contract) · inheritance (reuse) · polymorphism (same `.area()`, different result).

**Dataclasses**
- `@dataclass` writes `__init__`, `__repr__`, `__eq__` (compares values) from type-hinted fields.
- `field(default_factory=list)`, never `= []` (dataclass raises `ValueError`).
- `__post_init__` runs after the generated `__init__`: compute or validate fields.
- `frozen=True` → read-only + hashable. Gotcha: it also blocks assignments in your own `__post_init__`.
- Type hints are labels, not guards. **Dataclass** = trusted data inside my code; **Pydantic** = untrusted data from outside (API bodies, LLM output, config), validated and converted.

## Mistakes I made
- `day.weekday` without `()`; `pay` left as a string; `import datetime` inside the class.
- Mixed indentation (4/5/8/10 spaces) → format with Shift+Alt+F.
- Half marks: `__post_init__` purpose and dataclass vs Pydantic for an API body (8 Oct).

## Gaps
- [ ] [PYnative OOP exercises](https://pynative.com/python-object-oriented-programming-oop-exercise/) (~1 h).
- [ ] Re-test `__post_init__` + dataclass vs Pydantic (weak spot).
- [ ] Later: LeetCode design problems (Min Stack, LRU Cache).
