import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
turn off 660,55 through 986,197
turn off 341,304 t
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