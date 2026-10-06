"""See sys.path[0] change depending on WHICH FILE you run (5 min).

Run it twice and compare the first line:
  1. from learning-lab/:                python drill/modules/imports/syspath/where_am_i.py
  2. from drill/modules/imports/syspath/: python where_am_i.py
"""
import sys

# TODO 1: print sys.path[0] (the folder Python searches FIRST)

# TODO 2: print how many folders are in sys.path in total

# TODO 3: try to import my_module (it lives in drill/modules/, two folders up). Does it work? Why not?

# TODO 4: make it work with sys.path.append(...) pointing at drill/modules, then import my_module.
#         Then write one comment: why is sys.path.append a bad fix in real projects?
