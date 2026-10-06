"""Logging drill, step 5: a module that LOGS but never CONFIGURES logging."""
import logging

logger = logging.getLogger(__name__)   # "mathutils" when imported, "__main__" if run directly


def divide(a, b):
    logger.info("dividing %s by %s", a, b)
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("division failed")
        return None
