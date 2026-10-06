"""Chapter 4: __init__.py makes mypackage a package and runs on its first import.

Importing functions here lets users write `from mypackage import add`
instead of `from mypackage.module1 import add`.
"""
from .module1 import add
from .module2 import multiply
