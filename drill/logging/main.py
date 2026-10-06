"""Logging drill, step 5: the entry point, the ONLY place logging is configured.

Run (from learning-lab/):  python drill/logging/main.py
"""
import logging

from mathutils import divide   # works because this script's folder is sys.path[0]

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
    )
    print(divide(10, 2))
    print(divide(5, 0))

# Q1: why do the log lines say "mathutils", not "__main__"?
#     The logger was created in mathutils, and mathutils was IMPORTED, so its __name__ is "mathutils".
# Q2: a logger created in THIS file would show "__main__", because main.py is run directly.
