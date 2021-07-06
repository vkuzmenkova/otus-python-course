import os
from pathlib import Path
import functools
import itertools

cwd = os.getcwd()
print(cwd)
print(os.path.dirname(__file__))


@functools.lru_cache
def fib(n):
    if n < 2:
        print(n)
        return n
    print(n)
    return fib(n - 1) + fib(n - 2)


def add(x, y):
    return x + y


p_add = functools.partial(add, 2)
print(p_add(10))
print(fib(5))
