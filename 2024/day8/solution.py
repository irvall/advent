from collections import defaultdict
import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [list(line.rstrip()) for line in open(file_to_read, 'r').readlines()]

locations = defaultdict(list)
antinodes = set()

def inside(y,x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])

def add_antinodes(y, x, dy, dx):
    while inside(y, x):
        antinodes.add((y,x))
        y, x = y+dy, x+dx

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if not lines[y][x].isalnum(): continue
        antenna = lines[y][x]
        for (oy,ox) in locations[antenna]:
            dy, dx = oy-y, ox-x
            add_antinodes(y, x, dy, dx)
            add_antinodes(oy, ox, -dy, -dx)
        locations[antenna].append((y,x))
print(len(antinodes))