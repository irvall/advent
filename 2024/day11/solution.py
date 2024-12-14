import sys
from collections import defaultdict

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

stones = defaultdict(int)
stones |= {int(x): 1 for x in lines[0].split()}

def make_stones(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    mid = len(stone_str) // 2
    if len(stone_str) % 2 == 0:
        return [int(stone_str[:mid]), int(stone_str[mid:])]
    return [stone * 2024]

for i in range(75):
    for stone,freq in list(stones.items()):
        for ns in make_stones(stone):
            stones[ns] += freq
        stones[stone] -= freq
        
print(sum(stones.values()))
