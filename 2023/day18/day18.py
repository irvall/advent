from collections import deque
import sys
is_test = len(sys.argv) > 1
lines = [line.rstrip() for line in open('mini.txt' if is_test else 'input.txt', 'r').readlines()]
g = {}

def bfs(yx, minx, maxx, miny, maxy):
    q = deque()
    q.append(yx)
    steps = 0
    while q:
        y, x = q.popleft()
        if y == miny or y == maxy or x == minx or x == maxx:
            return 0
        ds = [(y, min(x+1, maxx)), (min(y+1, maxy), x), (y, max(x-1, minx)), (max(y-1, miny), x)]
        for yx in ds:
            if yx in g: continue
            g[yx] = steps
            q.append(yx)
            steps += 1
    return steps

x, y = 0, 0
minx, miny = 0, 0
maxx, maxy = 0, 0
for line in lines:
    d, s, _ = line.split()
    step = int(s)
    for i in range(step):
        if   d == 'L': x -= 1
        elif d == 'U': y -= 1
        elif d == 'R': x += 1
        else:          y += 1
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        g[(y,x)] = step
edge = len(g)

inside = 0
yxs = [(y,x) for x in range(minx,maxx+1) for y in range(miny, maxy+1)]
for yx in yxs:
    if yx in g: continue
    inside = max(inside, bfs(yx, minx, maxx, miny, maxy))
print(edge + inside)