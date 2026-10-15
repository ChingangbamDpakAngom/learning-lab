# argparse (CLI)

**Status:** ✅ done · **Sessions:** 10–15 Oct (no day folder; summary in [LEARNED.md](../LEARNED.md#13-argparse-cli--1015-oct)) · **Code:** [`drill/cli/`](../../drill/cli/) (argparse_basics.py, wordcount.py)
**Interview Qs:** [short answers](../INTERVIEW-QA.md#argparse-cli)
**Resources:** NeuralNine *Argument Parsing with argparse* (whole) · anthonywritescode *argparse tutorial #044* (`main(argv) -> int` pattern)

## Must know
- Create a parser → `add_argument` for every input → `parse_args(argv)` once → read `args.x`.
- Positional (no dashes) = compulsory · `--name` = optional, falls back to `default` (or `None`) · `action="store_true"` = flag (True if typed).
- `type=int` converts; `choices=[...]` restricts.
- Free: `--help`, type conversion, clear errors with exit code 2.
- Pattern: `def main(argv=None) -> int:` + `raise SystemExit(main())` → tests pass a list instead of the terminal; the int is the exit code (0 = success) that shells and CI check.

## Mistakes I made
- None recorded yet.

## Gaps
- [ ] Subcommands (`add_subparsers`): skipped, look up when needed.
- [ ] Use it for real in lab 01 (`--month`, `--rows`, `--out`, `--verbose`).
