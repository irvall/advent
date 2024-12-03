import sys, re

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
ans = 0
enable = True
for line in lines:
    matches = re.findall(r'((don\'t|do)\(\))|mul\((\d+),(\d+)\)', line)
    for (d, m, d1, d2) in matches: 
        if d: enable = d == 'do()'
        elif enable and d1:
            a,b = int(d1), int(d2)
            ans += (a*b)
print(ans)