# Python core

**Status:** ✅ done (quiz 5/7) · **Sessions:** [28 Sep](../../../log/2026-09-28_w1-d1/notes.md)
**Cheat sheet:** [Python core](Python-Core-Cheat-Sheet.jpg) · **Interview Qs:** [short answers](../../INTERVIEW-QA.md#python-core)

## Must know
- Default args are evaluated **once**, when `def` runs → `items=[]` is shared across calls. Use `items=None`.
- Names are references: `b = a` doesn't copy. `a.copy()` / `list(a)` = shallow; `copy.deepcopy` for nested data.
- tuple: immutable → hashable → usable as a dict key / set member. Unpacking: `name, cost = row`.
- dict: O(1) average lookup via hashing, insertion-ordered. `.get(k, 0)`, `Counter`, `defaultdict(list)`.
- set: unique items, O(1) `in`, `& | -`.
- Comprehensions `[f(x) for x in xs if cond]`; `( ... )` = lazy generator for big data. Too complex → write a loop.
- Truthiness: `0`, `""`, `[]`, `{}`, `None` are falsy. `if n % 2` means "if n is odd".
- `sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:3]` = top 3 by value.

## Mistakes I made
- Truthiness: didn't read `if n % 2` as "odd".
- Didn't state the cost of the alternative (list `in` is O(n) per check).
- Didn't read `key=` and `reverse=` to say *which* 3 items.

## Gaps
- [ ] `*args/**kwargs`: ticked in SKILLS-CHECKLIST but never noted or quizzed.
- [ ] Generators + `yield`, decorators, the GIL (Sun 18 Oct).
- [ ] Writing your own context manager (`__enter__`/`__exit__` or `contextlib.contextmanager`): the usual follow-up to "what does `with` do?".
- [ ] Interview one-liners not in the notes: `enumerate`, `zip`, `lambda`, `is` vs `==`.
- [ ] No interview-question file (only the [short answers](../../INTERVIEW-QA.md#python-core)).
