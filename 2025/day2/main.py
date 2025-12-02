import sys

use_test = len(sys.argv) > 1
file_name = 'test.txt' if use_test else "input.txt" 
ranges = open(file_name, "r").readline().split(',')

"""
990244-1009337,5518069-5608946,34273134-34397466,3
"""

def repeats(v):
    s = str(v)
    n = len(s)
    for step in range(1, n // 2 + 1):
        if n % step == 0:
            if s == s[:step] * (n // step):
                return True
    return False

res = sum(
    k
    for r in ranges
    for start, end in (map(int, r.split('-')),)
    for k in range(start, end + 1)
    if repeats(k)
)
print(res)