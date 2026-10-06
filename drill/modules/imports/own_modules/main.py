"""Chapters 2–5: every way to import your own code.

Run from this folder (own_modules/):  python main.py
"""
# 2. Local file: mymodule.py sits next to this script, so it's found via sys.path[0]
import mymodule

# 3. Module inside a package: full dotted path
from mypackage.module1 import add

# 4. Thanks to mypackage/__init__.py, the short form works too
from mypackage import multiply

# 5. Nested submodule: one more level in the dotted path
from mypackage.subpackage.submodule import shout

print(mymodule.greet("Deepak"))   # Hello, Deepak!
print(add(2, 3))                  # 5
print(multiply(2, 3))             # 6
print(shout("imports work"))      # IMPORTS WORK!
