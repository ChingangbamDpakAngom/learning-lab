# Sat 3 Oct 2026 · Week 1, Day 6 (catch-up: Wednesday's topic)

## Learn · Logging ✅
- Videos: Corey Schafer *Logging Basics* + *Logging Advanced* (first ~10 min).
- Why not `print`: logs have **levels**, timestamps and source names, can be switched off, and can go to files or monitoring tools.
- Levels: `DEBUG < INFO < WARNING < ERROR < CRITICAL`. Default level is **WARNING** → `info()` / `debug()` are hidden until you lower it.
- Every module: `log = logging.getLogger(__name__)`. Only the **entry point** calls `logging.basicConfig(...)`.
- `basicConfig` only works the **first** time it's called. If an imported module calls it first, it silently sets the level/format/file for the whole program.
- `basicConfig(level=..., filename="app.log", format="%(asctime)s %(levelname)s %(name)s: %(message)s")`.
- Use lazy formatting `log.info("rows=%s", n)`, not f-strings. `log.exception("msg")` inside `except` logs the traceback automatically (level ERROR).
- Handler = **where** logs go (console, file); formatter = **how they look**. Concept only; `basicConfig` is enough for labs.
- Silence a noisy library: `logging.getLogger("urllib3").setLevel(logging.WARNING)`.
- Never log secrets (API keys, personal data).
- Generated: [Logging-Cheat-Sheet.jpg](Logging-Cheat-Sheet.jpg) · [Interview questions](Interview-Questions.md)

### Recall check: 1.5 / 2
| # | Question | My answer | Interview-ready version |
|---|---|---|---|
| 1 | Why `getLogger(__name__)` over `logging.info()`? | own logger per module, not the root ✅ | every line shows **which module** wrote it, and levels can be set per module |
| 2 | Why shouldn't an imported module call `basicConfig`? | it's root config, same issue ½ | `basicConfig` only applies on the **first** call, so the module would decide the config for the whole program and main's call is ignored |

## Drill · logging warm-up (`drill/logging/`) ⬜
1. `divide(a, b)`: INFO log of inputs; `log.exception` on `ZeroDivisionError`, return `None`.
2. Format with time, level, name.
3. Level → WARNING: INFO lines disappear.
4. `filename="app.log"`.
5. Split into `mathutils.py` (`getLogger(__name__)`) + `main.py` (`basicConfig`); logger name shows `mathutils`.

## Build · lab 01: what to log
| Event | Level |
|---|---|
| start (month, rows) | INFO |
| full request URL | DEBUG |
| retry (attempt, status, wait) | WARNING |
| skipped, file exists | INFO |
| gave up after 3 attempts | ERROR, then raise |
| saved (path, rows) | INFO |
- `--verbose` CLI flag switches INFO ↔ DEBUG.
