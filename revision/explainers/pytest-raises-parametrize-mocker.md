# pytest: `raises`, `parametrize` and `mocker`, explained simply

Each tool solves **one problem**. Learn the problem first; the syntax then makes sense.
Code: [`drill/testing/`](../../drill/testing/) · Video: [Tech With Tim: Pytest Tutorial](https://www.youtube.com/watch?v=EgpLj86ZHFQ) (0:00–30:24)

---

## 1. `pytest.raises`: "I EXPECT this to fail"

**The problem:** a normal test checks that the code works. But sometimes the correct behaviour *is* an error: `divide(10, 0)` should refuse. If you just call it in a test, the error crashes the test and pytest marks it **failed**, even though the code did the right thing.

**The idea:** tell pytest "an error is expected inside this block; that's a pass".

```python
def test_divide_by_zero():
    with pytest.raises(ValueError):   # inside here, I expect a ValueError
        divide(10, 0)                 # it raises → test PASSES
```

| What happens inside the block | Result |
|---|---|
| raises `ValueError` | ✅ pass (exactly what we wanted) |
| raises nothing | ❌ fail ("you were supposed to refuse!") |
| raises a different error (`TypeError`) | ❌ fail |

`match="cannot divide"` also checks the error **message**.

**Kid version:** "if I touch the hot stove, I *should* get burnt". Getting burnt proves the stove works.
**In an AI role:** a Pydantic model must reject bad LLM output; an API must reject a missing key; a retry must give up after 3 tries.

---

## 2. `@pytest.mark.parametrize`: "same test, many inputs"

**The problem:** checking `is_prime` on 1, 2, 3, 4 means four copy-pasted tests.

**The idea:** write the test once and give pytest a **table**: one row per case.

```python
@pytest.mark.parametrize("num, expected", [   # column names
    (1, False),                               # row 1 → one test run
    (2, True),                                # row 2
    (3, True),
    (4, False),
])
def test_is_prime(num, expected):             # each row fills these two parameters
    assert is_prime(num) == expected
```

**How to read it:**
1. `"num, expected"` names the **columns**.
2. Each tuple is **one row** = one separate test run.
3. pytest calls `test_is_prime(1, False)`, then `test_is_prime(2, True)`, and so on.
4. The output shows each one: `test_is_prime[1-False] PASSED`, `test_is_prime[2-True] PASSED`…

**Kid version:** one quiz question ("is this number prime?") asked with four different numbers.
**In an AI role:** a text-cleaning function on 10 messy inputs, classifier thresholds, a prompt template with different variables.

---

## 3. `mocker`: "fake the outside world"

**The problem:** `get_weather("London")` calls a real website. In a test that's bad:
- slow, needs the internet;
- the site may be down → your test fails though *your* code is fine;
- with an LLM API, **every test run costs money**;
- the real answer changes daily, so you can't write a fixed `assert`.

**The idea:** for this one test, swap `requests.get` for a **fake** that returns whatever you say. Your code can't tell.

```python
def test_get_weather(mocker):
    fake_get = mocker.patch("main.requests.get")     # 1. swap the real one for a fake
    fake_get.return_value.status_code = 200          # 2. tell the fake what to answer
    fake_get.return_value.json.return_value = {"location": {"name": "London"}}

    result = get_weather("London")                   # 3. run YOUR code (it calls the fake)

    assert result["location"]["name"] == "London"    # 4. did your code read the answer right?
    fake_get.assert_called_once()                    # 5. did your code call it once?
```

**Line by line:**
1. `mocker.patch("main.requests.get")`: "inside `main`, replace `requests.get` with a fake". Use **`main.`** because that's where your code uses it.
2. `return_value`: "when someone calls the fake, hand back this". `get()` returns a response, so `.status_code` and `.json()` are faked on it.
3. Your real function runs; the fake answers instantly.
4. You test **your logic**, not the website.
5. The fake **remembers every call**, so you can check your code called it correctly (`assert_called_once_with(url)` checks the exact arguments).

When the test ends, `mocker` puts the real `requests.get` back automatically.
**Kid version:** a stunt double. The film can't tell, and nobody gets hurt.
**In an AI role:** you'll mock **LLM calls** constantly, to check *your* code builds the right prompt, parses the answer and handles a timeout, without paying for or waiting on a real model.

---

## What a junior AI engineer needs from pytest

| Level | Know it | Status |
|---|---|---|
| Must | `assert`, test naming, reading a failure | ✅ |
| Must | `pytest.raises` for error paths | ✅ |
| Must | Fixtures: fresh setup per test | ✅ |
| Must | `parametrize`: many cases, one test | ✅ |
| Must | Mocking external calls (APIs, LLMs, DBs) | ✅ basics |
| Should | `tmp_path` for file outputs | ✅ |
| Should (W3) | Testing a FastAPI endpoint with `TestClient` | coming |
| Should (W3) | Async tests (`pytest-asyncio`) for async LLM clients | coming |
| Know the idea (W4) | **Tests vs evals:** tests check *code* (pass/fail); evals check *LLM output quality* (scores) | coming |
| Skip | plugins, Hypothesis, complex fixture scopes | — |

**One sentence to remember:** tests check that my code is correct, mocks keep tests fast and free, and evals check that the model's answers are good.

## Self-check (answer out loud, then look)
> [!question]- Why can't you just call `divide(10, 0)` in a test without `pytest.raises`?
> The error would crash the test and pytest would mark it failed, even though refusing is the correct behaviour.

> [!question]- In `parametrize("num, expected", [...])`, what does one tuple become?
> One separate test run, with the tuple's values filled into the `num` and `expected` parameters.

> [!question]- Why mock `main.requests.get`, especially with an LLM API?
> Real calls are slow, can fail for reasons outside your code, change every time, and cost money. The mock gives a fixed, instant answer so you test only your own logic. Patch it where it's used (`main.`).
