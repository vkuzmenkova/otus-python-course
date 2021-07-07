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
# print(fib(5))

# for i in itertools.chain(['A', 'B', 'C'], ["4", "5", "6"]):
#     print(i)
# for i in itertools.count(10, 5):
#     if i > 100:
#         break
#     print(i)
# for i in itertools.cycle('ABC'):
#     print(i)
# for i in itertools.accumulate([1, 2, 3], lambda x, y: x + y ** 2):
#     print(i)
print(list(itertools.chain.from_iterable("ABC")))
