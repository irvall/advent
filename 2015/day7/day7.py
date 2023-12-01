import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
af AND ah -> ai
NOT lk -> ll
hz RSHIFT 1 -> is
NOT
"""

def part_one():
    ans = 0
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