import sys


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [list(line.rstrip()) for line in open(file_to_read, 'r').readlines()]
grid = []

rows = len(lines)
cols = len(lines[0])

def inside(x, y):
    return 0 <= x < cols and 0 <= y < rows

def lit_neighbours(x, y):
    ans = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if not inside(i, j) or i == x and j == y: continue
            nb = lines[j][i]
            ans += 1 if nb == '#' else 0
    return ans

def turn_on_corners(grid):
    grid[0][0] = '#'
    grid[0][cols-1] = '#'
    grid[rows - 1][0] = '#'
    grid[rows - 1][cols - 1] = '#'
    

def step():
    new_grid = []
    i = 0
    turn_on_corners(lines)
    for y in range(rows):
        new_grid.append([])
        for x in range(cols):
            is_lit = lines[y][x] == '#'
            lits = lit_neighbours(x,y)
            if is_lit:
                if lits == 2 or lits == 3:
                    new_grid[i].append('#')
                else:
                    new_grid[i].append('.')
            else:
                if lits == 3:
                    new_grid[i].append('#')
                else:
                    new_grid[i].append('.')
        i += 1
    turn_on_corners(new_grid)
    return new_grid

def total():
    res = 0
    global lines
    for row in lines:
        for ch in row:
            res += 1 if ch == '#' else 0
    return res

def pp():
    print()
    global lines
    for row in lines:
        for ch in row:
            print(ch, end='')
        print()
    print(total())
        
def animate(n):
    global lines
    for _ in range(n):
        #pp() 
        lines = step()
    #pp()
            
            
animate(100)
print(total())
    