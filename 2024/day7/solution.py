import sys
lines = [x.rstrip() for x in open(sys.argv[1], 'r').readlines()]

def solve(numbers, current, target):
  if len(numbers) == 0:
    return current == target
  head, *tail = numbers
  concat = int(str(current) + str(head))
  add = solve(tail, current+head, target)
  mul = solve(tail, current*head, target)
  con = solve(tail, concat, target)
  return add or mul or con

ans = 0
for line in lines:
  target, numbers = line.split(':')
  targetNumber = int(target)
  numbers = [int(_) for _ in numbers.split()]
  if solve(numbers, 0, targetNumber):
    ans += targetNumber
print(ans)
