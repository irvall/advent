import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
L = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

def inside(y, x):
    return 0 <= y < len(L) and 0 <= x < len(L[0])

def on_edge(y,x):
    return y in {0, len(L)-1} or x in {0, len(L[0])-1}

directions = [(j,i) for j in range(-1,2) for i in range(-1,2)]
D = [[(dy*i, dx*i) for i in range(1, 4)] for dy, dx in directions]
p1, p2 = 0, 0
for j in range(len(L)):
    for i in range(len(L[0])):
        if L[j][i] != 'X': continue
        for ds in D:
            q = list('SAM')
            for(dy,dx) in ds:
                y, x = dy+j, dx+i
                if not inside(y,x): break
                if q[-1] == L[y][x]:
                    q.pop()
            p1 += 1 if not q else 0
for j in range(len(L)):
    for i in range(len(L[0])):
        if on_edge(j,i) or L[j][i] != 'A': continue
        UL, LR = L[j-1][i-1], L[j+1][i+1]
        LL, UR = L[j+1][i-1], L[j-1][i+1]
        if (UL == 'M' and LR == 'S' or UL == 'S' and LR == 'M') and\
           (LL == 'M' and UR == 'S' or LL == 'S' and UR == 'M'):
               p2 += 1 
print(p1, p2)
