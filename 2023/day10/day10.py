import collections
lines = [_.rstrip() for _ in open('tricky1.txt', 'r').readlines()]
"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
y, x = 0, 0
maxx, maxy = len(lines[0]), len(lines)
for j in range(maxy):
    for i in range(maxx):
        ch = lines[j][i]
        if ch == 'S': y, x = j, i
T = True
F = False

southbound = {'|', 'F', '7', 'S'}
eastbound  = {'-', 'L', 'F', 'S'}
northbound = {'|', 'L', 'J', 'S'}
westbound  = {'-', 'J', '7', 'S'}

def find_loop(y, x):
    q = collections.deque()
    q.append((y,x, 0))
    seen = {}
    dist = 0
    while q:
        y, x, d = q.popleft()
        dist = max(d, dist)
        if (y,x) not in seen:
            seen[(y,x)] = dist
        pipe = lines[y][x]
        ds = [(1,0,0), (0,1, 1), (-1, 0, 2), (0, -1, 3)]
        for sj,si,c in ds:
            j, i = y+sj, x+si
            if not (0 <= j < maxy and 0 <= i < maxx) or (j,i) in seen:
                continue
            next = lines[j][i]
            tup = (j,i,d+1)
            if c == 0 and pipe   in southbound and next in northbound: # next is south
                q.append(tup)
            elif c == 1 and pipe in eastbound  and next in westbound: # next is east
                q.append(tup)
            elif c == 2 and pipe in northbound and next in southbound: # next is north
                q.append(tup)
            elif c == 3 and pipe in westbound  and next in eastbound: # next is west 
                q.append(tup)
    print('dist', dist)
    return seen

# 0 if not enclosed
def enclosed(y, x):
    q = collections.deque()
    q.append((y,x))
    seen = set()
    while q:
        y, x = q.popleft()
        if     y == 0 or y == maxy - 1 \
            or x == 0 or x == maxx - 1:
            return 0
            
        seen.add((y,x))
        current = lines[y][x]
        ds = [(1,0), (0,1), (-1, 0), (0, -1)]
        for sj,si in ds:
            j, i = y+sj, x+si
            if not (0 <= j < maxy and 0 <= i < maxx) or (j,i) in seen:
                continue
            next = lines[j][i]
            tup = (j,i)
            
    print('dist', dist)
    return seen



the_loop = find_loop(y,x)

for y in range(maxy):
    for x in range(maxx):
        if (y,x) in the_loop:
            print(f'{the_loop[(y,x)]}'.ljust(4), end='')
        else: print(lines[y][x].ljust(4), end='')
    print()




seen = set()
for y in range(maxy):
    for x in range(maxx):
        if lines[y][x] != '.' or (y,x) in seen:
            continue


            









            
