#pylint:allow-global-unused-variables=no
import sys
is_test = len(sys.argv) > 1
lines = [line.rstrip() for line in open('mini.txt' if is_test else 'input.txt', 'r').readlines()]

def area(x1, x2, y1, y2):
    a, b = x1*y2, y1*x2
    return (a - b) / 2


x, y = 0, 0
xys = [(x,y)]
wall = 0
for line in lines:
    _, _, color = line.split()
    color = color.strip('()#').strip()
    step = int(color[:5], 16)
    dir = int(color[-1], 16)
    match dir:
        case 0: x += step
        case 1: y += step
        case 2: x -= step
        case 3: y -= step
    wall += step
    xys.append((x,y))
foo = 'ss'
ans = 0
n = len(xys)
for i in range(n):
    p1, p2 = xys[i], xys[(i+1) % n]
    ans += area(*p1, *p2)

print(int(ans) + wall//2 + 1)
