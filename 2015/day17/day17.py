from collections import defaultdict


containers = [5, 5, 10, 15, 20]
containers = """11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3""".split('\n')
containers = [int(_) for _ in containers]
n = len(containers)

d = defaultdict(int)

def solve(liters, i, res, container_count):
    if liters == 0:
        d[container_count] += 1
        return 1 + res
    if i >= n or liters < 0:
        return res
    include = solve(liters - containers[i], i + 1, res, container_count + 1)
    exclude = solve(liters, i + 1, res, container_count)
    return include + exclude

print(solve(150, 0, 0, 0))
print(d)