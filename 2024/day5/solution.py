from collections import defaultdict
import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

rules, update = open(file_to_read, 'r').read().split('\n\n')

before = defaultdict(set)
for r in rules.split():
    a, b = (int(x) for x in r.split('|'))
    before[a].add(b)

p1, p2 = 0, 0
for u in update.split():
    N = [int(x) for x in u.split(',')]
    ok = True
    for i in range(len(N)):
        v = N[i]
        for j in range(0,i):
            w = N[j]
            if w in before[v]:
                ok = False
                N[i], N[j] = N[j], N[i]
    if ok:
        p1 += N[len(N)//2]
    if not ok:
        p2 += N[len(N)//2]

print(p1, p2)