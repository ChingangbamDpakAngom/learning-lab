"""Word counter CLI: argparse drill (W2).

Run from the repo root:
    uv run python drill/cli/wordcount.py --help
    uv run python drill/cli/wordcount.py drill/cli/sample.txt --top 3
    uv run python drill/cli/wordcount.py drill/cli/sample.txt --top 3 --ignore-case

Step 1. In build_parser(), create an ArgumentParser with a one-line description.
Step 2. Add a positional argument `path` (the text file to read), with type=Path and a help text.
Step 3. Add an optional `--top` (an int, default 5, help text that shows the default).
Step 4. Add a flag `--ignore-case` that is False unless given (look up action="store_true").
Step 5. In main(): parse the args. If the file does not exist, call parser.error(...) with a clear message.
Step 6. Read the file, split it into words (lowercase them only if --ignore-case),
        count them with collections.Counter, and print the top N as "word: count", one per line.
Step 7. Run --help and check that every argument shows its help text.

Expected (--top 3 --ignore-case):
    the: 4
    data: 3
    nhs: 2
"""

import argparse
from collections import Counter
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Count the most common words in a text file.")
    parser.add_argument("path", type=Path, help="text file to read")
    parser.add_argument("--top", type=int, default=5, help="how many words to show (default: %(default)s)")
    parser.add_argument("--ignore-case", action="store_true", help="treat 'The' and 'the' as the same word")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.path.exists():
        parser.error(f"file not found: {args.path}")

    text = args.path.read_text(encoding="utf-8")
    if args.ignore_case:
        text = text.lower()

    for word, count in Counter(text.split()).most_common(args.top):
        print(f"{word}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
