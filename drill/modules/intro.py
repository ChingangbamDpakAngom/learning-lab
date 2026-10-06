"""Import styles, sys.path and a few standard-library modules.

Run from this folder:  python intro.py
"""
import sys

import my_module                         # 1. whole module: use my_module.find_index
import my_module as mm                   # 2. alias: same module object, shorter name
from my_module import find_index, test   # 3. specific names straight into this file

courses = ["History", "Math", "Physics", "CompSci"]

print(my_module.find_index(courses, "Math"))   # 1
print(mm.find_index(courses, "Physics"))       # 2
print(find_index(courses, "CompSci"), test)    # 3
print(mm is my_module)  # True: "Imported my_module..." printed only once (modules are cached)

# Where Python looks for imports, in order. The first entry is THIS script's folder,
# which is why `from mathutils import divide` works but `from drill.logging...` didn't.
for path in sys.path:
    print(path)

# A few standard-library modules: no install needed
import random, math, datetime, calendar, os

print(random.choice(courses))
print(math.sqrt(16), math.radians(90))
print(datetime.date.today(), calendar.isleap(2028))
print(os.getcwd())          # the folder you ran the command from
print(os.__file__)          # where the os module itself lives on disk
