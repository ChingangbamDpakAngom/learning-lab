# Logging

**Status:** ✅ done (recall 1.5/2) · **Sessions:** [3 Oct](../../../log/2026-10-03_w1-d6/notes.md) · [6 Oct, drill step 5](../../../log/2026-10-06_w2-d2/notes.md) · **Code:** [`drill/logging/`](../../../drill/logging)
**Cheat sheet:** [Logging](Logging-Cheat-Sheet.jpg) · **Interview Qs:** [3 Oct set](Interview-Questions.md) · [short answers](../../INTERVIEW-QA.md#logging)
**Resources:** Corey Schafer *Logging Basics* (whole) · *Logging Advanced* (first ~10 min)

## Must know
- Why not `print`: levels, timestamps, source name, can be switched off, can go to files/monitoring.
- `DEBUG < INFO < WARNING < ERROR < CRITICAL`. Default is **WARNING** → `info()` hidden until you lower it.
- Every module: `log = logging.getLogger(__name__)`. Only the **entry point** calls `logging.basicConfig(...)`.
- `basicConfig` only works on the **first** call → an imported module calling it would set the config for the whole program.
- `basicConfig(level=..., filename="app.log", format="%(asctime)s %(levelname)s %(name)s: %(message)s")`.
- Lazy formatting `log.info("rows=%s", n)`. `log.exception("msg")` inside `except` logs the traceback (level ERROR).
- Handler = **where** logs go; formatter = **how they look** (concept only).
- Silence a noisy library: `logging.getLogger("urllib3").setLevel(logging.WARNING)`. Never log secrets.
- What to log in a job: start INFO · request URL DEBUG · retry WARNING · gave up ERROR then raise · saved INFO; `--verbose` switches INFO ↔ DEBUG.

## Mistakes I made
- Half marks on "why shouldn't an imported module call `basicConfig`": the point is **first call wins**, so main's own config is ignored.
- Drill step 5: `ModuleNotFoundError` from `import drill.logging.mathutils` (the script's folder is on `sys.path`, not the repo root).

## Gaps
- [ ] Handlers/formatters in code (concept only so far; `basicConfig` is enough for labs).
- [ ] Structured (JSON) logs + request IDs: concept, comes back in W7 observability.
