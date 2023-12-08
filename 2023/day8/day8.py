import math
import functools

lr, nodes = open('input.txt', 'r').read().split('\n\n')
indices = [0 if d == 'L' else 1 for d in lr]
n = len(indices)
g = {}
entries = []
for line in nodes.split('\n'):
    nd, pair = (_.strip() for _ in line.split('='))
    l, r = (_.strip() for _ in pair[1:-1].split(','))
    if nd.endswith('A'): 
        entries.append(nd)
    g[nd] = [l, r]

def part_one():
    i = 0
    entry = 'AAA'
    while entry != 'ZZZ':
        entry = g[entry][indices[i % n]]
        i += 1
    return i 

def part_two():
    steps = []
    for entry in entries:
        i = 0
        satisfied = False
        while not satisfied:
            satisfied = True
            entry = g[entry][indices[i % n]]
            if entry[2] != 'Z': 
                satisfied = False
            i += 1
        steps.append(i)
    return functools.reduce(math.lcm, steps)

print(part_one())
print(part_two())