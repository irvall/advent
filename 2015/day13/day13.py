from itertools import permutations
import re, sys
from collections import defaultdict, deque
from queue import Queue

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
pattern = re.compile(r'(\w+)\D+(gain|lose) (\d+).*\b(\w+).')

options = defaultdict(dict)


for line in lines:
    match = pattern.match(line)
    if match:
        person1, sign, value, person2 = match.groups()
        options[person1][person2] = int(value) if sign == 'gain' else -int(value)
        options['ME'][person2] = 0
        options[person1]['ME'] = 0
    

def calculate_happiness(seating):
    happiness = 0
    for i in range(len(seating)):
        x = options[seating[i]][seating[i-1]]
        y = options[seating[i]][seating[(i+1)%len(seating)]]
        happiness += x + y
    return happiness

def find_best_seating():
    max_happiness = 0
    print(options.keys())
    for seating in permutations(options.keys()):
        max_happiness = max(max_happiness, calculate_happiness(seating))
    return max_happiness

print(find_best_seating())

# # too high
# # 888
        
    