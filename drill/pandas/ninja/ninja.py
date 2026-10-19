"""pandas ninja: 17 offline pandas challenges (input table -> expected table).

Challenges come from https://github.com/dridk/pandas-ninja (cloned into
drill/pandas/ninja/pandas-ninja, not committed). You solve them in solutions.py.

Run from the repo root:
    uv run python drill/pandas/ninja/ninja.py              # list all + which pass
    uv run python drill/pandas/ninja/ninja.py square-it    # show one + check your answer
"""

import importlib.util
import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
CHALLENGES = HERE / "pandas-ninja" / "public"


def load_solutions():
    spec = importlib.util.spec_from_file_location("solutions", HERE / "solutions.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(file: str, solutions, verbose: bool) -> str:
    data = json.loads((CHALLENGES / "challenges" / file).read_text(encoding="utf-8"))
    df = pd.DataFrame(data["input"])
    expected = pd.DataFrame(data["expected"])
    func = getattr(solutions, Path(file).stem.replace("-", "_"))

    if verbose:
        print(f"== {data['name']} ==\n{data['placeholder'].strip()}\n")
        print(f"INPUT ({len(df)} rows):\n{df.head(10)}\n")
        print(f"EXPECTED ({len(expected)} rows):\n{expected.head(10)}\n")

    result = func(df.copy())
    if result is None:
        return "todo"
    try:
        pd.testing.assert_frame_equal(
            pd.DataFrame(result).reset_index(drop=True), expected,
            check_dtype=False, check_exact=False, atol=0.01,
        )
    except AssertionError as err:
        if verbose:
            print(f"YOURS:\n{pd.DataFrame(result).head(10)}\n\n{err}")
        return "FAIL"
    return "PASS"


def main() -> int:
    solutions = load_solutions()
    index = json.loads((CHALLENGES / "challenges.json").read_text(encoding="utf-8"))["data"]

    if len(sys.argv) > 1:
        file = sys.argv[1] if sys.argv[1].endswith(".json") else f"{sys.argv[1]}.json"
        print(check(file, solutions, verbose=True))
        return 0

    for item in index:
        status = check(item["file"], solutions, verbose=False)
        print(f"{status:5} {item['level']:7} {Path(item['file']).stem}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
