from collections import deque
import sys
from functools import reduce
sys.setrecursionlimit(5000)

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

def inside(x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)

N = "North"
E = "East"
S = "South"
W = "West"

def neighbours(x, y):
    ns = []
    # slipping = slip(x,y)
    # if slipping: return [slipping]
    if inside(x-1, y) and lines[y][x-1] not in {'#'}:# '>'}:
        ns.append((x-1,y))
    if inside(x+1, y) and lines[y][x+1] not in {'#'}:# '<'}:
        ns.append((x+1,y))
    if inside(x, y-1) and lines[y-1][x] not in {'#'}:# 'v'}:
        ns.append((x,y-1))
    if inside(x, y+1) and lines[y+1][x] not in {'#'}:# '^'}:
        ns.append((x,y+1))
    return ns
       
# def slip(x,y):
#     c = lines[y][x]
#     if   c == '>': return (x+1, y)
#     elif c == '<': return (x-1, y)
#     elif c == '^': return (x, y-1)
#     elif c == 'v': return (x, y+1)
#     return None

# def pp(visited, standing):
#     print()
#     for j in range(len(lines)):
#         for i in range(len(lines[0])):
#             if standing == (i,j):
#                 print('@', end='')
#             elif (i,j) in visited:
#                 print('-', end='')
#             else: print('·' if lines[j][i] == '.' else lines[j][i], end='')
#         print()
#     print()

n_map = {}

def dfs(start):
    stack = [(start, [start])]
    longest_path = []
    distances = set()
    sx, sy = start
    seen = set()
    assert(lines[sy][sx] == 's')
    while stack:
        (x,y), path = stack.pop()
       
        if lines[y][x] == 'e':
            if len(path) > len(longest_path):
                longest_path = path
                d = len(longest_path) - 1
                if d not in distances:
                    distances.add(d)
                    print(d)
            continue
        
        ns = n_map[(x,y)] if (x,y) in n_map else neighbours(x,y)
        if (x,y) not in n_map:
            n_map[(x,y)] = ns
        
        seen.add((x,y))
        for n in ns:
            if n not in path and n not in seen:
                stack.append((n, path + [n]))
        seen.remove((x,y))
    return longest_path
    
print(len(dfs((1,0))) - 1)

# 6334 - too low