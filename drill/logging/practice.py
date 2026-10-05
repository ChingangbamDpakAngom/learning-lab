"""Logging warm-up drill, step 1: log inputs and failures in divide().

Run:  python drill/logging/practice.py
"""
import logging

# TODO 1: create a module-level logger named after this module
log = logging.getLogger(__name__)

def divide(a, b):
    # TODO 2: log at INFO: "dividing %s by %s" with a and b (lazy %s args, not an f-string)
    log.info("dividing %s by %s",a,b)
    try:
        # TODO 3: return the result of a / b
        return a/b
    except ZeroDivisionError:
        # TODO 4: log "division failed" with the method that also records the traceback
        # TODO 5: return None
        log.exception("division failed")
        return None
        


if __name__ == "__main__":
    # TODO 6: configure logging ONCE here so INFO messages are shown
    logging.basicConfig(filename='app.log',
                        level=logging.INFO, 
                        format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s' )
    # STEP 2 · TODO 7: add format= so each line shows time, level, logger name, message
    #                  (attributes: asctime, levelname, name, message → "%(attr)s")
    # STEP 3 · TODO 8: change the level to WARNING and run: which lines disappear, and why?
    #                  Then set it back to INFO.
    logging.basicConfig(filename='app.log',
                            level=logging.WARNING, 
                            format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s' )
    # STEP 4 · TODO 9: add filename="app.log": where do the logs go now? Open app.log.
    print(divide(10, 2))   # expect 5.0
    print(divide(5, 0))    # expect None (plus an ERROR log with a traceback)
