import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]
X = lines[0]

"""
^><^>>>^<^v<v^^vv^><<^<><<vv^<>^<^v>^vv<>v><vv^^<>
"""

def part_one():
    ans = 0
    seen = set()
    x, y = 0, 0
    for d in X:
        if (x,y) not in seen:
            ans += 1
            seen.add((x,y))
        match d:
            case '>': x += 1
            case '<': x -= 1
            case '^': y += 1
            case 'v': y -= 1
    return ans


def part_two():
    ans = 0
    seen = set()
    x, y = 0, 0
    x1, y1 = 0, 0
    santa = True
    for d in X:
        if (x,y) not in seen:
            ans += 1
            seen.add((x,y))
        if (x1,y1) not in seen:
            ans += 1
            seen.add((x1,y1))
        match d:
            case '>': 
                if santa: x += 1 
                else: x1 += 1
            case '<': 
                if santa: x -= 1
                else: x1 -= 1
            case '^': 
                if santa: y += 1;
                else: y1 += 1
            case 'v': 
                if santa: y -= 1
                else: y1 -= 1
        santa = not santa
    return ans



if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)