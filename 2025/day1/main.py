import sys

use_test = len(sys.argv) > 1
file_name = "input.txt" if not use_test else "test.txt"
lines = [_.rstrip() for _ in open(file_name, "r")]

"""
L25
L8
L44
L6
R1
R26
"""

dial = 50
c = 0
for line in lines:
    d = line[0]
    v = int(line[1:])
    for _ in range(v):
        if d == 'R':
            dial += 1
        else:
            dial -= 1
        dial %= 100
        if dial == 0:
            c += 1

print(dial, c)