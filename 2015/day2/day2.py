import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

"""
20x3x11
15x27x5
6x29x7
30x15x9
19x29x21
10x4x15
"""
def part_one():
    ans = 0
    for line in lines:
        l, w, h = [int(side) for side in line.split('x')]
        s1, s2, s3 = l*w, w*h, h*l
        ans += 2*s1+2*s2+2*s3 + min(s1,s2,s3)
    return ans

def part_two():
    ans = 0
    for line in lines:
        l, w, h = [int(side) for side in line.split('x')]
        min_side = min(l,w,h)
        mid_side = min(max(l,w), max(w,h))
        ans += min_side*2 + mid_side*2
        ans += l*w*h
    return ans


if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)