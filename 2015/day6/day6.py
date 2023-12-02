import sys, re

use_test_data = False
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
turn off 660,55 through 986,197
turn off 341,304 t
"""

def part_one():
    ans = 0
    pattern = r'\d+'
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        x1, y1, x2, y2 = (int(_) for _ in re.findall(pattern, line))
        turn_on = 'on' in line
        while y1 <= y2:
            while x1 <= x2:
                if turn_on:
                    lights[y1][x1] = True
                else:
                    toggle = 'toggle' in line
                    lights[y1][x1] = not lights[y1][x1] if toggle else False
                x1 += 1
            y1 += 1
    for row in lights:
        for b in row:
            ans += 1 if b else 0
    return ans

def part_two():
    ans = 0
    ...
    return ans


if __name__ == '__main__':
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
