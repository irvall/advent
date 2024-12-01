from collections import defaultdict
import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

ls, rs = [], []
rfreq = defaultdict(int)

for line in lines:
    lnum, rnum = [int(_) for _ in line.split()]
    ls.append(lnum)
    rs.append(rnum)
    rfreq[rnum] += 1
    
dist = sum(abs(a-b) for a,b in zip(sorted(ls), sorted(rs)))
print(dist)

score = sum(l * rfreq[l] for l in ls)
print(score)