"""Logging drill, step 5: a module that LOGS but never CONFIGURES logging."""
import logging

# TODO 1: create this module's logger (same line as practice.py)
logger = logging.getLogger(__name__)

def divide(a, b):
    # TODO 2: log at INFO: "dividing %s by %s" with a and b (lazy %s args, not an f-string)
    logger.info("dividing %s by %s", a, b)
    try:
        # TODO 3: return the result of a / b
        return a/b
    except ZeroDivisionError:
        # TODO 4: log "division failed" with the method that also records the traceback
        # TODO 5: return None
        logger.exception("division failed")
        return None

# Rule: no basicConfig in this file. Modules only create loggers.
