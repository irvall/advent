from collections import defaultdict, namedtuple
import math
import sys

use_test = len(sys.argv) > 1
file_name = 'test.txt' if use_test else "input.txt"
lines = [_.rstrip() for _ in open(file_name, "r")]

Point = namedtuple('Point', 'x y z')

def dist(p: Point, q: Point):
    return math.sqrt((p.x-q.x)**2 + (p.y-q.y)**2 + (p.z-q.z)**2)

P = []
for line in lines:
    P.append(Point(*map(int,line.split(','),))) 

D = []
for i,p in enumerate(P):
    for j,q in enumerate(P):
        if i >= j: continue
        D.append((i,j,dist(p,q)))
D.sort(key=lambda tup: tup[2])

parent = list(range(len(P)))
def find(i):
    if i == parent[i]:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(p,q):
    parent[find(p)] = find(q)

def p1():
    count = defaultdict(int)
    for p in parent:
        count[find(p)] += 1
    values = sorted(count.values())[-3:]
    return math.prod(values)
    
components = len(P)
for i,(p,q,_) in enumerate(D):
    if i == (10 if use_test else 1000):
        print(p1())
    if find(p) != find(q):
        union(p,q)
        components -= 1
    if components == 1:
        print(P[p].x*P[q].x)
        break
