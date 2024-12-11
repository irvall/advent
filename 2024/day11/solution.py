import sys


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

numbers = [int(x) for x in lines[0].split()]


def insert(idx, number, numbers, replace = False):
    v = numbers[:idx] + [number] + numbers[idx + 1 if replace else idx:]
    return v

"""
If the stone is engraved with the number 0, it is replaced by a stone engraved
with the number 1.

If the stone is engraved with a number that has an even number of numbers, it is
replaced by two stones. The left half of the numbers are engraved on the new left
stone, and the right half of the numbers are engraved on the new right stone.
(The new numbers don't keep extra leading zeroes: 1000 would become stones 10
and 0.)

If none of the other rules apply, the stone is replaced by a new stone; the old
stone's number multiplied by 2024 is engraved on the new stone.

"""
blinks = 75
for _ in range(blinks):
    i = 0
    while i < len(numbers):
        d = numbers[i]
        num_string = str(d)
        digits = len(num_string)
        if d == 0:
            numbers = insert(i, 1, numbers, True)
        elif digits % 2 == 0:
            a, b = num_string[:digits//2], num_string[digits//2:]
            numbers = insert(i, int(a), numbers)
            numbers = insert(i+1, int(b), numbers, replace=True)
            i += 1
        else:
            numbers = insert(i, d*2024, numbers, replace=True)
        i += 1

print(len(numbers))