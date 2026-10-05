# Fri 2 Oct 2026 · Week 1, Day 5 (catch-up: Tuesday's topic)

## Learn · Error handling + file I/O ✅
- Catch the **narrowest** exception you can actually handle; let the rest propagate. Never `except:` or `except Exception: pass`.
- `try / except / else / finally`: `else` runs only if nothing was raised; `finally` always runs (cleanup).
- `raise ValueError("bad file") from e` keeps the original cause in the traceback. Raise early with a clear message.
- Custom exception (`class DownloadError(Exception): pass`) when callers need to tell your errors apart.
- `with open(...)` closes the file **even if an exception happens** halfway through.
- `pathlib`: `Path("data") / "raw"`, `.mkdir(parents=True, exist_ok=True)`, `.exists()`, `.suffix`, `.stem`, `.glob("*.csv")`, `.read_text()` / `.write_text()`.
- CSV: `csv.DictReader` / `DictWriter`, always `newline=""` + `encoding="utf-8"` (Windows default encoding differs → classic bug). JSON: `json.loads` / `json.dumps(indent=2)`.
- Retries: retry only **transient** errors (timeouts, 5xx, 429) with exponential backoff (1s, 2s, 4s) and a cap on attempts. Never retry 404 / bad input: it fails the same way every time.
- Generated: [Error-Handling-File-IO-Cheat-Sheet.jpg](Error-Handling-File-IO-Cheat-Sheet.jpg) · [Interview questions](Interview-Questions.md)

### Quick check: 3 / 3
| # | Question | My answer | Interview-ready version |
|---|---|---|---|
| 1 | Why is `except Exception: pass` dangerous? | hides errors silently ✅ | ...and the program carries on with bad/missing data, the failure shows up later somewhere unrelated, and the traceback is gone |
| 2 | What does `with open()` guarantee? | closes the file after the operation ✅ | closes it **even if an exception is raised** inside the block |
| 3 | 404 vs 503: retry? | 404 never, 5xx yes ✅ | also retry timeouts + 429; use backoff; cap attempts |

**Mistakes to remember:** say *why* it matters (silent bad data), and *even if an error happens* for `with`.

## How much to memorise (for interviews)
1. **Type from memory:** loops, functions, list/dict/set ops, comprehensions, slicing, f-strings, `try/except`, `with open`, basic SQL. Comes from repetition, not memorising.
2. **Know it exists, look it up:** library arguments (`DictWriter`, pathlib methods, pandas options, Docker flags).
3. **Explain out loud:** the *why* and the trade-offs. This is what interviews actually grade.
- Method: build > read · test yourself before re-reading · review after 1 day, 3 days, 1 week · think out loud in live coding.

## Build · 01 NHSBSA downloader: spec ✅
- Step 1: explore the CKAN API (`package_show?id=english-prescribing-data-epd`, `datastore_search?resource_id=EPD_YYYYMM&limit=5`).
- Step 2: `download_month(month, rows, out_dir) -> Path`: validate `YYYYMM`, retry timeouts/5xx/429 ×3 with backoff, raise `DownloadError`, write CSV with `DictWriter`, create `out_dir`, skip if the file exists (idempotent).

## Apply · CV v2 polish ✅
- Aegis injection-guard bullet now states the real numbers (100% precision, 37% recall). Never overclaim: interviewers dig into every line.
- Internship bullet rewritten without invented numbers. Prepare a 1-minute "tell me about your internship" answer.
- ⬜ Phone number, final PDF, 2 applications.
