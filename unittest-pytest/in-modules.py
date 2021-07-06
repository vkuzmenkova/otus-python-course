import os
from pathlib import Path
from functools import wraps
import itertools

cwd = os.getcwd()
print(cwd)
print(os.path.dirname(__file__))

root = Path('/')
print(root.parent.parent)
