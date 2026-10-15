"""argparse code-along (W2): type the video's examples here, then do wordcount.py.

Run from the repo root:
    uv run python drill/cli/argparse_basics.py --help

Step 1. Code along with the video: one positional argument, then print it.
Step 2. Add an optional argument with type=int and a default; run it with and without the option.
Step 3. Add a flag with action="store_true"; print args to see the Namespace.
Step 4. Run --help, then run with a wrong type (e.g. a word where an int is expected) and read the error.
Step 5. Move on to wordcount.py (Steps 1-7 in its docstring).
"""

import argparse
import pprint
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    # Basics
    parser = argparse.ArgumentParser()
    # positional arguments
    parser.add_argument("test", help = "testing out my first basic feature I have used")
    parser.add_argument("square", type = int, 
                         help = "provide the square of a number provided")
    args = parser.parse_args(argv)
    print(args.test)
    print(args.square**2)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())



