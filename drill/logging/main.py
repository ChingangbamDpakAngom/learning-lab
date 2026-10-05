"""Logging drill, step 5: the entry point. The ONLY place logging is configured.

Run (from learning-lab/):  python drill/logging/main.py
"""
import logging

# TODO 3: import divide from mathutils
from drill.logging.mathutils import divide

if __name__ == "__main__":
    # TODO 4: basicConfig with level INFO and your step-2 format (console this time, no filename)
    logging.basicConfig(level = logging.INFO, format = '%(message)s')
    print(divide(10, 2))
    print(divide(5, 0))

# After running, answer:
#   Q1: what logger name appears in the output now, and why did it change from __main__?
#   Q2: add  log = logging.getLogger(__name__)  here and log.info("starting")
#       before the divide calls. What name does THAT line show?
