import sys, re
from collections import defaultdict

use_test = False
if len(sys.argv) > 1:
    use_test = True

lines = [_.rstrip() for _ in open('mini.txt' if use_test else 'input.txt').readlines()]
input_patt = re.compile(r'#(\d+) @ (\d+),(\d+). (\d+)x(\d+)')

"""
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""
ans = 0
grid = defaultdict(int)
for line in lines:
    #1  1, 3: 4x 4
    id, x, y, w, h = (int(_) for _ in input_patt.match(line).groups())
    for j in range(y, y+h):
        for i in range(x, x+w):
            grid[(j,i)] += 1

print(sum((1 for _,v in grid.items() if v >= 2)))
for line in lines:
    id, x, y, w, h = (int(_) for _ in input_patt.match(line).groups())
    ok = True
    for j in range(y, y+h):
        for i in range(x, x+w):
            if grid[(j,i)] > 1:
                ok = False
                break
        if not ok:
            break
    if ok:
        print(id)






        


