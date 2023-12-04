import sys

use_test_data = False 
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
Card   1: 99 71 95 70 36 79 78 84 31 10 |  5 45 54
"""

def part_one():
    ans = 0
    for line in lines:
        card, numbers = line.split(':')
        scratch, winning = (set(_.split()) for _ in numbers.split('|'))
        hits = scratch.intersection(winning)
        ps = 1 if hits else 0
        for _ in range(len(hits) - 1):
            ps *= 2
        ans += ps
    return ans

def part_two():
    ans = 1
    freq = {}
    for line in lines:
        card, numbers = line.split(':')
        _, card_id = card.split()
        card_id = int(card_id)
        scratch, winning = (set(_.split()) for _ in numbers.split('|'))
        hits = scratch.intersection(winning)
        matches = len(hits)
        times = 1 if card_id not in freq else freq[card_id]
        while times > 0:
            for i in range(card_id, card_id + matches + 1):
                if i not in freq:
                    freq[i] = 1
                else:
                    freq[i] += 1
            times -= 1

    print(freq)
    return sum(freq.values())


if __name__ == '__main__':  
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)

# too low
# 14152603