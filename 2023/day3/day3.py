import re

use_test_data = False
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
.........232.633.......................803........
"""

def part_one():
    ans = 0
    text = ''.join(lines)
    total_lines = len(lines)
    line_len = len(lines[0])
    for number in re.finditer(r'\d+', text):
        num = int(number.group())
        start, end = number.span()
        n = end-start + 1
        x, y = start % line_len, start // total_lines
        found = False
        for j in range(max(0, y-1), min(total_lines, y+2)):
            for i in range(max(0, x-1), min(line_len, x+n)):
                ch = lines[j][i]
                if ch.isnumeric() or ch == '.': continue
                ans += num
                found = True
                break
        if found: break
    return ans

def part_two():
    text = ''.join(lines)
    total_lines = len(lines)
    line_len = len(lines[0])
    gears = {}
    for number in re.finditer(r'\d+', text):
        num = int(number.group())
        start, end = number.span()
        n = end-start + 1
        x,y = start % line_len, start // total_lines
        found = False
        for j in range(max(0, y-1), min(total_lines, y+2)):
            for i in range(max(0, x-1), min(line_len, x+n)):
                if lines[j][i] != '*': continue
                if (j,i) in gears: gears[(j,i)].append(num)
                else: gears[(j,i)] = [num]
                found = True
                break
            if found: break
    values = [a * b for values in gears.values() if len(values) == 2 for a, b in [values]]
    return sum(values)

if __name__ == '__main__':
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
