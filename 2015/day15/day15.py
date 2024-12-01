from itertools import permutations
import re, sys
from collections import defaultdict, deque
from queue import Queue
from functools import reduce

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
xs = []
for i in range(len(lines)):
    line = lines[i]
    ingredient, recipe = line.split(':')
    items = recipe.split(',')
    print(items)
    if len(xs) != (len(items)):
        for j in range(len(items)):
            xs.append([])
    for j in range(len(items)):
        item = items[j]
        x, num = item.strip().split()
        xs[j].append(int(num))

def calc(xs, ys):
    res = 0
    zipped = list(zip(xs,ys))
    for i in range(len(zipped)):
        x, y = zipped[i]
        res += x*y
    return res


def perm(size, target):
    res = []
    def inner(arr, sum, idx):
        if idx == len(arr)-1:
            arr[idx] = sum
            res.append(arr.copy())
            return
        for i in range(sum + 1):
            arr[idx] = i
            inner(arr, sum-i, idx+1)
    inner([0 for _ in range(size)], target, 0)
    return res

perms = perm(len(xs[0]), 100)
record = -999999
rs = []
for p in perms:
    res = 1
    cal = 0
    ns = []
    for x in xs:
        ns.append(max(0, calc(x, p)))
    record = record if ns[-1] != 500 else max(record, reduce(lambda x,y: x*y, ns[:-1]))
print(record)
    