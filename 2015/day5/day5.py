import sys
import re
use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

twice = re.compile(r'(\w)\1')
repeat = re.compile(r'(.).\1')
pair = re.compile(r'(.)(.).*\1\2')
vowel = re.compile(r'(?:[aeiou].*){3}')
forbidden = ['ab', 'cd', 'pq', 'xy']

""" Puzzle input sneak peek:
sszojmmrrkwuftyv
isaljhemltsdzlum
fujcyucsrxgatisb
"""

def is_nice(string):
    for f in forbidden:
        if f in string: 
            return False
    return twice.search(string) and vowel.search(string)

def is_nice_two(string):
    return pair.search(string) and repeat.search(string)

def part_one():
    ans = 0
    for line in lines:
        ans += 1 if is_nice(line.strip()) else 0
    return ans

def part_two():
    ans = 0
    for line in lines:
        ans += 1 if is_nice_two(line.strip()) else 0
    return ans

if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)


