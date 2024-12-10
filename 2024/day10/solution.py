from collections import deque
import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [[int(x) for x in line.rstrip()] for line in open(file_to_read, 'r').readlines()]
starting_pos = []

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 0:
            starting_pos.append((y,x))

def inside(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])

def bfs(root):
    seen = set([root])
    Q = deque([root])
    p1, p2 = 0, 0
    while Q:
        y, x = Q.popleft()
        if lines[y][x] == 9:
            p2 += 1
            if (y,x) not in seen:
                p1 += 1
        seen.add((y,x))
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ty, tx = y+dy, x+dx
            if not inside(ty, tx) or (ty,tx) in seen: continue
            if (lines[ty][tx] - lines[y][x]) == 1:
                Q.append((ty,tx))
    return p1, p2

p1, p2 = 0, 0
for sp in starting_pos:
    v1, v2 = bfs(sp)
    p1 += v1
    p2 += v2
print(p1, p2)



