from collections import deque
import sys
use_test = len(sys.argv) > 1
file_name = "input.txt" if not use_test else "test.txt"
lines = [line.rstrip() for line in open(file_name, "r").readlines()]
G = [[c for c in line] for line in lines]
R, C = len(G[0]), len(G)
sy, sx = 0, lines[0].find('S')

def splits(y, x):
    Q = deque()
    Q.append((y, x))
    S = set()
    count = 0
    while Q:
        (y,x) = Q.popleft()
        if y == C or (y,x) in S:
           continue 
        S.add((y,x))
        if G[y][x] == '^':
            Q.append((y,x-1))
            Q.append((y,x+1))
            count += 1
        else:
            Q.append((y+1,x))
    return count

DP = {}
def ways(y, x):
    if (y,x) in DP:
        return DP[(y,x)]
    if y+1 == C:
        return 1
    if G[y][x] == '^':
        res = ways(y, x+1) + ways(y, x-1)
        DP[(y,x)] = res
        return res
    res = ways(y+1, x)    
    DP[(y,x)] = res
    return res

print(splits(sy,sx))
print(ways(sy, sx))