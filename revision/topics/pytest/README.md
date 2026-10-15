# pytest

**Status:** ✅ done (16 tests passing) · **Sessions:** [8 Oct](../../../log/2026-10-08_w2-d4/notes.md) · **Code:** [`drill/testing/`](../../../drill/testing)
**Explainer:** [raises, parametrize, mocker](../../explainers/pytest-raises-parametrize-mocker.md) · **Interview Qs:** [short answers](../../INTERVIEW-QA.md#pytest)
**Resources:** Tech With Tim *Pytest Tutorial* (0:00–30:24) · pytest `tmp_path` docs

## Must know
| Tool | Why | How |
|---|---|---|
| `assert` | prove the right answer | `assert add(2, 3) == 5` |
| `pytest.raises` | the error path matters too | `with pytest.raises(ValueError, match="..."):` |
| fixture (+ `yield`) | fresh setup per test, no shared state | `@pytest.fixture`; test asks for it by parameter name; after `yield` = cleanup |
| `parametrize` | many cases, one test | `@pytest.mark.parametrize("num, expected", [...])` |
| `tmp_path` | never touch real files | `save_totals(rows, tmp_path / "totals.csv")` |
| `mocker` | no real API / DB calls | `mocker.patch("main.requests.get")`, `return_value`, `assert_called_once_with` |

- Interview-ready depth: happy path + error path + mocked external call.
- Patch where the name is **used** (`main.requests.get`), not where it's defined.

## Mistakes I made
- Commented out the fixture → `fixture 'user_manager' not found`: a parameter means "give me the fixture with this name"; globals don't count.
- A global object shared by tests leaked data between them → fixtures give a clean one each.
- `ModuleNotFoundError: requests` despite mocking: the library must still be installed (`uv add requests`, not `--dev`).
- Mock checks are exact: `"Users.db"` vs `"User.db"` failed.

## Gaps
- [ ] Test discovery + running: `test_*.py` files, `test_` functions, `pytest -k name`, `-x`, `-v` (SKILLS-CHECKLIST item, not in notes).
- [ ] `monkeypatch` (env vars, attributes) vs `mocker`: checklist asks for "mocking HTTP (monkeypatch / respx)".
- [ ] No cheat sheet, no interview-question file (only the [short answers](../../INTERVIEW-QA.md#pytest)).
- [ ] Skipped until W3: `conftest.py`, fixture scopes, skip/xfail, coverage, async tests.
- [ ] Use it for real in lab 01 tests.
