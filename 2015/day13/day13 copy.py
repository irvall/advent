import re, sys
from collections import defaultdict
from queue import Queue

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

                     r'(.*) would (gain|lose) ([0-9]+).* (.*).
pattern = re.compile(r'(\w+)\D+(gain|lose) (\d+).*\b(\w+).')

options = defaultdict(list)
for line in lines:
    name1, gain_lose, units, name2 = pattern.match(line).groups()
    units = int(units) if gain_lose == 'gain' else -int(units)
    options[name1].append((name2, units))

def bfs(root, distances):
    Q = []
    explored = set()
    explored.add(root)
    Q.append(root)
    name, dist = root
    while Q:
        v, distance = Q.pop(0)
        for (name, units) in options[v]:
            if name not in explored:
                new_dist = units + distance
                Q.append((name, new_dist))
                if name in distances:
                    if distances[name] > new_dist:
                        distances[name] = new_dist
                else:
                    distances[name] = new_dist
                explored.add(name)


for name in options.keys():
    distances = {}
    bfs((name, 0), distances)
    del distances[name]
    print(distances, sum(distances.values()))
