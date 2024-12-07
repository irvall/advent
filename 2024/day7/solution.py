import sys
lines = [x.rstrip() for x in open(sys.argv[1], 'r').readlines()]

def solve(numbers, current, target, i):
  if len(numbers) == 0:
    return current == target
  head, *tail = numbers
  concat = int(str(current) + str(head))
  add = solve(tail, current+head, target, i+1)
  mul = solve(tail, current*head, target, i+1)
  con = solve(tail, concat, target, i+1)
  return add or mul or con

ans = 0
for line in lines:
  target, numbers = line.split(':')
  targetNumber = int(target)
  numbers = [int(_) for _ in numbers.split()]
  if solve(numbers, 0, targetNumber, 0):
    ans += targetNumber
print(ans)
