import math

lines = open("input.txt", 'r').readlines()
grid = [[c for c in line.rstrip('\n')] for line in lines]

s = ''
for c in range(len(grid[0])):
    for r in range(len(grid)-1):
        s += grid[r][c]
    s += '-'

problems = iter(s.replace(' ', '').rstrip('-').split('--'))
operators = lines[-1].replace(' ', '')

ans = 0
for op in operators:
    numbers = list(map(int, next(problems).split('-')))
    ans += sum(numbers) if op == '+' else math.prod(numbers)

print(ans)