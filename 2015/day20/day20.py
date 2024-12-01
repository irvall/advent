
from collections import defaultdict


def f(n):
    foo = defaultdict(int)
    for i in range(1, n//10):
        for j in range(i, n//10):
            foo[j] += i*10
    return foo