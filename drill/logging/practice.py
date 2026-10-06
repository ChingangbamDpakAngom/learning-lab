"""Logging drill, steps 1–4: one file that logs and configures itself.

Run (from learning-lab/):  python drill/logging/practice.py  → logs go to app.log
"""
import logging

log = logging.getLogger(__name__)   # one logger per module, named after it


def divide(a, b):
    log.info("dividing %s by %s", a, b)   # lazy %s args, not an f-string
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("division failed")  # ERROR level + full traceback
        return None


if __name__ == "__main__":
    # Configure ONCE, in the entry point. basicConfig only works the FIRST time it's called:
    # a second call (e.g. level=WARNING) is silently ignored.
    logging.basicConfig(
        filename="app.log",   # step 4: file instead of console (appends; path is relative to where you run)
        level=logging.INFO,   # step 3: WARNING would hide the two INFO lines
        format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",   # step 2
    )
    print(divide(10, 2))   # 5.0
    print(divide(5, 0))    # None (+ ERROR with traceback in app.log)
