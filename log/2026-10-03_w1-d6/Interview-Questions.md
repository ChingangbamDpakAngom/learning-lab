# W1 · D6 Interview Questions · Logging

How to use: read the question, **say your answer out loud**, then open the callout. Mark ✅ / ½ / ❌ in the score table. Redo the ❌ ones tomorrow.

Levels: 🟢 screening call · 🟡 technical round · 🔴 follow-up probe

---

> [!question]- Q1 🟢 Why use logging instead of `print`?
> Logs have levels you can turn on or off without editing code, timestamps, and the name of the module that wrote them. They can go to the console, a file or a monitoring tool. `print` has none of that.

> [!question]- Q2 🟢 Name the log levels in order. What's the default?
> `DEBUG < INFO < WARNING < ERROR < CRITICAL`. The default is **WARNING**, so `info()` and `debug()` show nothing until you lower the level. A level shows itself and everything above it.

> [!question]- Q3 🟡 Why `log = logging.getLogger(__name__)` instead of `logging.info(...)`?
> Each module gets its own named logger, so every line shows **which module** wrote it, and levels can be set per module (e.g. silence `urllib3`, keep your own code at DEBUG). `logging.info` writes through the root logger with no source name.

> [!question]- Q4 🟡 Where should logging be configured, and why?
> Once, in the entry point (`main`). `basicConfig` only applies on the **first** call, so if an imported module called it, that module would silently decide the level, format and destination for the whole program. Modules and libraries only create loggers.

> [!question]- Q5 🟡 What does `log.exception("msg")` do?
> Logs `msg` at ERROR level **plus the full traceback** of the exception currently being handled. Use it inside an `except` block.

> [!question]- Q6 🟡 Why `log.info("rows=%s", n)` rather than an f-string?
> With `%s` arguments the message string is only built if that level is enabled, so disabled DEBUG lines cost almost nothing. It also keeps the message template constant, which helps log search tools group lines.

> [!question]- Q7 🟡 What would you log in a data-download client?
> Start and finish at INFO (month, row count, path), the full URL at DEBUG, each retry at WARNING (attempt, status, wait), the final failure at ERROR before raising. Never API keys or personal data.

> [!question]- Q8 🔴 What are structured logs and request IDs, and why do production systems use them?
> Logs written as JSON fields (time, level, request_id, latency, status) instead of free text, so they can be filtered and aggregated. A request ID is attached to every line for one request, so you can follow it across services. Aegis does both.

---

| Q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Attempt 1 | | | | | | | | |
| Attempt 2 | | | | | | | | |
