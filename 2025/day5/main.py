import sys

the_ranges, _ = open('input.txt', 'r').read().split('\n\n')

ranges = []
for line in the_ranges.split('\n'):
    a, b = map(int, line.split('-'))
    ranges.append((a, b + 1))

ranges.sort()  

ans = 0
current_max = ranges[0][0]
for start, end in ranges:
    new_ids = end - max(current_max, start)
    if new_ids > 0:
        ans += new_ids
        current_max = end

print(ans)