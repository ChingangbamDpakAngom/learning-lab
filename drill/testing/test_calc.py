"""pytest drill: test the functions in calc.py.
Read: https://docs.pytest.org/en/stable/getting-started.html (10 min)

Setup (once, from learning-lab/):
    uv init --bare
    uv add --dev pytest
Run (from learning-lab/):
    uv run pytest drill/testing -v

Steps:
  Step 1. Import add from calc. Write test_add() that asserts add(2, 3) == 5.
          Run it and see it pass. Then change 5 to 6, run again, and read
          how pytest shows the failure. Change it back.
  Step 2. Write test_divide() for a normal case: divide(10, 2) == 5.
  Step 3. Write test_divide_by_zero() using
              with pytest.raises(ValueError):
          Question: why can't you just call divide(1, 0) and assert something?
  Step 4. Use @pytest.mark.parametrize to test is_even with 4 cases in ONE test:
          (2, True), (3, False), (0, True), (-4, True).
          Question: what do you gain over writing 4 separate tests?
  Step 5. Test save_totals with the built-in tmp_path fixture:
          def test_save_totals(tmp_path): ...
          Save [("2026-09", 120)] to tmp_path / "totals.csv", then assert the
          file exists and its text contains "2026-09,120".
          Question: why use tmp_path instead of a real folder?
"""
import pytest

from calc import add, divide, is_prime, save_totals

# Why unit tests?
# - cover most of the code
# - prove each small component works on its own
# - catch it when a later change breaks something

def test_add():
    assert add(2, 3) == 5, "2 + 3 should equal 5"
    assert add(-1, 1) == 0, "-1 + 1 should equal 0"
    assert add(0, 0) == 0, "0 + 0 should equal 0"       

def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected, f"{num} should be {'prime' if expected else 'not prime'}"

def test_save_totals(tmp_path):
    # tmp_path = a fresh temporary folder per test, deleted by pytest later
    out = save_totals([("2026-09", 120)], tmp_path / "totals.csv")

    assert out.exists()
    assert "2026-09,120" in out.read_text(encoding="utf-8")
