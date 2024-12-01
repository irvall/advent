sy, sx = 0, 0
y = 0
g = []
for line in open('mini.txt', 'r'):
    line = line.strip()
    if not line.strip(): break
    if 'S' in line:
        sx = line.find('S')
        sy = y
    y += 1
    g.append([c for c in line])

maxy = len(g)
maxx = len(g[0])

def pp(new_yxs):
    bloop_count = 0
    for y in range(maxy):
        for x in range(maxx):
            if (y,x) in new_yxs:
                bloop_count += 1
                print('O', end='')
            else:
                print('.', end='')
        print()
    print('bloop count', bloop_count)



def bfs(yxs, steps):
    once = True
    while steps > 0:
        steps -= 1
        new_yxs = set()
        for y,x in yxs:
            if y >= maxy and x >= maxx and once:
                once = False
                print('JUST HAP')
                pp(new_yxs)
            ds = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
            for j, i in ds:
                j1 = j % maxy
                i1 = i % maxx
                if g[j1][i1] == '#': continue
                new_yxs.add((j,i))
        
        if len(new_yxs) > 0:
            pp(new_yxs)
        yxs = new_yxs
    return len(yxs)

print(bfs([(sy,sx)], 50))
print(bfs([(sy,sx)], 100))







