from collections import defaultdict

use_test_data = False
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
Card   1: 99 71 95 70 36 79 78 84 31 10 |  5 45 54
"""

def part_one():
    ans = 0
    for line in lines:
        _, numbers = line.split(':')
        scratch, winning = (set(_.split()) for _ in numbers.split('|'))
        hits = scratch.intersection(winning)
        ps = 1 if hits else 0
        for _ in range(len(hits) - 1):
            ps *= 2
        ans += ps
    return ans

def part_two():
    freq = defaultdict(int)
    for line in lines:
        card, numbers = line.split(':')
        card_id = int(card.split()[1])
        scratch, ticket = (set(_.split()) for _ in numbers.split('|'))
        copies = len(scratch & ticket)
        freq[card_id] += 1
        for i in range(card_id + 1, card_id + copies + 1):
            freq[i] += freq[card_id]
    return sum(freq.values())


if __name__ == '__main__':
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
