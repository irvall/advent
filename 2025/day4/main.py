import sys

use_test = len(sys.argv) > 1
file_name = "input.txt" if not use_test else "test.txt"
lines = [_.rstrip() for _ in open(file_name, "r")]
grid = [list(line) for line in lines]
w = len(grid[0])
h = len(grid)

def reachable(y, x):
    rolls = 0
    for j in range(y-1, y+2):
        if not (0 <= j < h): continue
        for i in range(x-1, x+2):
            if (j,i) == (y,x) or not (0 <= i < w): 
                continue
            if grid[j][i] == '@': 
                rolls += 1
            if rolls >= 4:
                return False
    return rolls < 4

def remove():
    to_remove = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.' : continue
            if reachable(y, x):
                to_remove.append((y, x))
    
    for y, x in to_remove:
        grid[y][x] = '.'
    
    return len(to_remove)

res = 0
while True:
    removeable = remove()
    if removeable == 0:
        break
    res += removeable
print(res)
    


