import sys, re

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
eight9fhstbssrplmdlncmmqqnklb39ninejz
three656
ppj
"""

def part_one():
    ans = 0
    for line in lines:
        num = ''
        for ch in line:
            if ch.isdigit():
                num += ch
                break
        for ch in reversed(line):
            if ch.isdigit():
                num += ch
                break
        ans += int(num)
    return ans

def part_two():
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    pattern = re.compile(f"(?=({'|'.join(nums)}|\d))")
    ans = 0
    for line in lines:
        matches = pattern.findall(line)
        first, last = matches[0], matches[-1]
        if not first.isnumeric(): first = str(nums.index(first) + 1)
        if not last.isnumeric():  last  = str(nums.index(last) + 1)
        ans += int(first + last)
    return ans


if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
