from collections import defaultdict, deque
import itertools
import sys


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
N,S,E,W = 0, 1, 2, 3

def valid(y,x):
    return 0<=y<len(lines) and 0<=x<len(lines[0]) and lines[y][x] != '#'

dir1 = [(1,0,S), (0,1,E), (-1,0,W), (0,-1,N)]
dir2 = [(0,1,E), (-1,0,W), (0,-1,N), (1,0,S)]
dir3 = [(-1,0,W), (0,-1,N), (1,0,S), (0,1,E)]
dir4 = [(0,-1,N), (1,0,S), (0,1,E), (-1,0,W)]
INF = 999999999
def default_factory():
    return INF
t = 7036
t = 109496
def search(sy,sx):
    Q = deque()
    Q.append((sy,sx,E,0,0,[(sy,sx)]))
    seen = defaultdict(lambda: INF)
    paths = set()
    while Q:
        (y,x,orientation,cost,angles,path) = Q.popleft()
        if lines[y][x] == 'E' and cost == t:
            print(cost, len(path))
            paths |= set(path)
        seen[(y,x)] = cost
        for dy,dx,o in dir4:
            ny,nx = y+dy, x+dx
            new_cost = cost + 1 + (1000 if o!=orientation else 0)
            current_cost = seen[(ny,nx)]
            if current_cost >= t and new_cost > t: continue
            if valid(ny,nx):
                Q.append((ny,nx,o,new_cost,0,path+[(ny,nx)]))
    print(len(paths))

sy, sx = None, None
for y,line in enumerate(lines):
    if 'S' in line:
        sx = line.index('S')
        sy = y
        break

search(sy,sx)
    


