import sys

use_test_data = False 
X = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')][0]


def part_one():
    cnt = 0
    for ch in X:
        cnt += 1 if ch == '(' else -1
    return cnt

        

def part_two():
    cnt = 0
    pos = 0
    for ch in X:
        pos += 1
        cnt += 1 if ch == '(' else -1
        if cnt == -1:
            return pos
    return -1

if __name__ == '__main__':
    p1 = part_one()
    p2 = part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)