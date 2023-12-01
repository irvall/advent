import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
2000
12013
5489
11485
2430
7722
5456

6693
3867
16
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