from collections import defaultdict
import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [list(line.rstrip()) for line in open(file_to_read, 'r').readlines()]

locations = defaultdict(list)
antinodes = set()

def inside(y,x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if not lines[y][x].isalnum(): continue
        antenna = lines[y][x]
        for (oy,ox) in locations[antenna]:
            if (y,x) == (oy,ox): continue
            dy, dx = oy-y, ox-x
            ty, tx = y, x
            while inside(ty,tx):
                antinodes.add((ty,tx))
                ty, tx = ty+dy, tx+dx
            while inside(oy,ox):
                antinodes.add((oy,ox))
                oy, ox = oy-dy, ox-dx
        locations[antenna].append((y,x))
print(len(antinodes))