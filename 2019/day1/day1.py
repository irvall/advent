import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
127117
121199
80494
83466
125933
80813
137787
1226
"""

def part_one():
    ans = 0
    for line in lines:
        ...
    return ans

def part_two():
    ans = 0
    ...
    return ans


if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)