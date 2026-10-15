# Errors, file I/O, retries

**Status:** ✅ done (quick check 3/3) · **Sessions:** [2 Oct](../../log/2026-10-02_w1-d5/notes.md)
**Cheat sheet:** [Error handling + file I/O](../../log/2026-10-02_w1-d5/Error-Handling-File-IO-Cheat-Sheet.jpg) · **Interview Qs:** [2 Oct set](../../log/2026-10-02_w1-d5/Interview-Questions.md) · [short answers](../INTERVIEW-QA.md#errors--file-io)

## Must know
- Catch the **narrowest** exception you can handle; let the rest propagate. Never bare `except:` or `except Exception: pass`.
- `try / except / else / finally`: `else` only if nothing was raised; `finally` always (cleanup).
- `raise ValueError("bad file") from e` keeps the original cause. Raise early with a clear message.
- Custom exception (`class DownloadError(Exception)`) when callers need to tell your errors apart.
- `with open(...)` closes the file **even if an exception happens** inside the block.
- `pathlib`: `Path("data") / "raw"`, `.mkdir(parents=True, exist_ok=True)`, `.exists()`, `.suffix`, `.stem`, `.glob("*.csv")`, `.read_text()`.
- CSV: `DictReader` / `DictWriter` with `newline=""` + `encoding="utf-8"`. JSON: `json.loads` / `json.dumps(indent=2)`.
- Retry only **transient** errors (timeouts, 5xx, 429) with exponential backoff and a cap. Never retry 404 / bad input.
- Idempotent: skip the work if the output file already exists.

## Mistakes I made
- Answers were right but short: say *why* (`except: pass` → silent bad data, failure shows up later, traceback lost) and *even if an error happens* for `with`.

## Gaps
- [ ] Use it for real in lab 01 (`download_month` with retries + `DownloadError`).
