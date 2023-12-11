from collections import namedtuple
import sys
lines = [list(line.rstrip()) for line in open('input.txt', 'r').readlines()]
factor = 1000000
empty_cols = set()
empty_rows = set()
galaxies = set()
galaxy = namedtuple('galaxy', 'x y')

for i in range(len(lines)):
    if '#' not in lines[i]:
        empty_rows.add(i)

for i in range(len(lines[0])):
    empty_col = True
    for j in range(len(lines)):
        if lines[j][i] == '#':
            empty_col = False
            galaxies.add(galaxy(j,i))
    if empty_col:
        empty_cols.add(i)

def distance(g1,g2):
    res = 0
    for x in range(min(g1.x, g2.x), max(g1.x,g2.x)):
        if x in empty_rows:
            res += factor
        else: res += 1
    for y in range(min(g1.y, g2.y), max(g1.y,g2.y)):
        if y in empty_cols:
            res += factor
        else: res += 1
    return res

sums = []
seen = set()
for g1 in galaxies:
    for g2 in galaxies:
        if g1 == g2 or (g1,g2) in seen: continue
        seen.add((g2,g1))
        sums.append(distance(g2,g1))

print(sum(sums))