from itertools import permutations
import re, sys
from collections import defaultdict, deque
from queue import Queue
from functools import reduce

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')

target_sue = {}

for line in tape:
    category, num = line.split(':')
    target_sue[category] = int(num)
    
def matches(items):
    res = 0
    gt = set(['cats', 'trees'])
    lt = set(['pomeranians', 'goldfish'])
    for item in items:
        category, num = [_.strip() for _ in item.split()]
        num = int(num)
        if category in gt and target_sue[category] < num:
            res += 1
        elif category in lt and target_sue[category] > num:
            res += 1
        elif target_sue[category] == num and category not in lt.union(gt):
            res += 1
    return res

record = -9999
record_id = None
for line in lines:
    sue_id = int(line.split(':')[0][3:])
    items = line.split(':')
    items = ''.join(items[1:]).split(',')
    res = matches(items)
    if res > record:
        record = res
        record_id = sue_id
    
print(target_sue) 
print(record_id, record)
    

