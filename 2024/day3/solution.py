import sys, re

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
ans = 0
enable = True
for line in lines:
    muls = re.findall(r'((don\'t|do)\(\))|(mul\(\d*,\d*\))', line)
    for (d,_,m) in muls:
        if d: enable = d == 'do()'
        elif enable and m:
            m = m.replace('mul(', '')
            m = m.replace(')', '')
            a,b = (int(x) for x in m.split(','))
            ans += (a*b)
print(ans)