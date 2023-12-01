import sys
import hashlib

use_test_data = False
X = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')][0]


""" Puzzle input sneak peek:
iwrupvqb

"""

def part_one():
    i = 0
    target = '00000'
    while True:
        m = hashlib.md5()
        key = X + str(i)
        m.update(str.encode(key))
        hex_string = m.hexdigest()
        if hex_string.startswith(target):
            return key
        i += 1
    return 'err' 

def part_two():
    i = 0
    target = '000000'
    while True:
        m = hashlib.md5()
        key = X + str(i)
        m.update(str.encode(key))
        hex_string = m.hexdigest()
        if hex_string.startswith(target):
            return key
        i += 1
    return 'err' 


if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
