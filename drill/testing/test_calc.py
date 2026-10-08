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
