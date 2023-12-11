from collections import defaultdict, deque
import sys
lines = [list(_.rstrip()) for _ in open('tricky.txt', 'r').readlines()]



x, y = 0, -1
s_found = False
max_x, max_y = len(lines[0]), len(lines)
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.north = None
        self.south = None
        self.east  = None
        self.west  = None

    def __repr__(self) -> str:
        sb = f'\nNode({self.x}, {self.y})'
        sb += f'\nnorth: {self.north}'
        sb += f'\nsouth: {self.south}'
        sb += f'\neast: {self.east}'
        sb += f'\nwest: {self.west}\n'
        return sb

    def adj(self):
        return [self.north, self.south, self.east, self.west]

start = None
g = {}
for y in range(max_y):
    for x in range(max_x):
        if lines[y][x] == '.': continue
        nd = Node(x,y)
        ns = [(min(x+1,max_x-1),y), (max(x-1,0),y), (x,min(y+1, max_y-1)), (x,max(y-1, 0))]
        for i, j in ns:
            if (i,j) == (x,y) or lines[j][i] == '.': continue
            nb = (j,i)
            if lines[j][i] == 'S':
                start = nb
            if lines[j][i] == '|' and x == i:
                (nd.south if y < j else nd.north).append(nb)
            elif lines[j][i] == '-' and y == j:
                (nd.east if x < i else nd.west).append(nb)
            elif lines[j][i] == 'L' and (y == j and x > i) or (x == i and y < j):
                (nd.west if y == j else nd.south).append(nb)
            elif lines[j][i] == 'J' and (y == j and x < i) or (x == i and y < j):
                (nd.east if y == j else nd.south).append(nb)
            elif lines[j][i] == '7' and (y == j and x < i) or (x == i and y > j):
                (nd.east if y == j else nd.north).append(nb)
            elif lines[j][i] == 'F' and (y == j and x > i) or (x == i and y > j):
                (nd.west if y == j else nd.north).append(nb)
        g[(y,x)] = nd

print(g)
