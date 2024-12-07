import sys
lines = [x.rstrip() for x in open(sys.argv[1], 'r').readlines()]

def solve(numbers, current, target):
  if current > target: return 0
  if not numbers:
    return target if current == target else 0
  head, *tail = numbers
  concat = int(str(current) + str(head))
  return solve(tail, current+head, target) or \
    solve(tail, current*head, target) or \
    solve(tail, concat, target)

ans = 0
for line in lines:
  target, numbers = line.split(':')
  targetNumber = int(target)
  numbers = [int(_) for _ in numbers.split()]
  ans += solve(numbers, 0, targetNumber)
print(ans)