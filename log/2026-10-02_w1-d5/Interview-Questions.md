# W1 · D5 Interview Questions · Error handling · File I/O · Retries

How to use: read the question, **say your answer out loud**, then open the callout. Mark ✅ / ½ / ❌ in the score table. Redo the ❌ ones tomorrow.

Levels: 🟢 screening call · 🟡 technical round · 🔴 follow-up probe

---

> [!question]- Q1 🟢 Why is `except Exception: pass` a bad idea?
> It hides every error, including bugs like typos. The program carries on with missing or wrong data, the failure shows up later somewhere unrelated, and the traceback you'd need to debug it is gone. Catch the narrowest exception you can actually handle and let the rest propagate.

> [!question]- Q2 🟢 What's the difference between `else` and `finally` in a try block?
> `else` runs only if the `try` block raised nothing. `finally` runs **always**, whether there was an exception or not, so it's for cleanup (closing files, releasing locks).

> [!question]- Q3 🟢 What does `with open(...)` guarantee?
> The file is closed when the block ends, **even if an exception is raised** inside it. It works for anything with cleanup: files, DB connections, HTTP sessions, locks.

> [!question]- Q4 🟡 What does `raise ValueError("...") from e` do, and why use it?
> It raises a new, clearer error while chaining the original as its cause (`__cause__`). The traceback shows both, so you get a meaningful message *and* the root cause.

> [!question]- Q5 🟡 When would you write a custom exception class?
> When callers need to handle your errors differently from built-in ones: e.g. `DownloadError` lets the CLI print a friendly message and exit, while real bugs still crash loudly. Keep it simple: `class DownloadError(Exception): pass`.

> [!question]- Q6 🟡 Your API call fails. Which errors do you retry, and how?
> Retry **transient** errors only: timeouts, 5xx and 429 (rate limited, honour `Retry-After`). Never 4xx like 400/401/404: the same request fails the same way. Use exponential backoff (1s, 2s, 4s), cap the attempts (e.g. 3), log every retry, and set a `timeout=` on every request.

> [!question]- Q7 🟡 Why pass `encoding="utf-8"` and `newline=""` when writing CSV?
> Windows' default encoding isn't UTF-8, so non-ASCII text (drug names, £) can crash or corrupt. `newline=""` stops the csv module writing blank lines between rows on Windows.

> [!question]- Q8 🔴 What does "idempotent" mean for a data download job?
> Running it twice has the same effect as running it once. E.g. skip the download if the file for that month already exists, or overwrite atomically; never append duplicates. It makes retries and scheduled re-runs safe.

---

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Attempt 1 | | | | | | | | |
| Attempt 2 | | | | | | | | |
