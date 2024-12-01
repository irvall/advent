import sys
sys.setrecursionlimit(5000)

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

arr = [int(_) for _ in lines[0].split()]

seen = {}

def distribute(arr, count):
    global seen
    key = ','.join(str(_) for _ in arr)
    if key in seen:
        return count - seen[key]
    seen[key] = count
    n = len(arr)
    i = arr.index(max(arr))
    j = (i+1) % n 
    while arr[i] != 0:
        arr[i] -= 1
        arr[j] += 1
        j = (j+1) % n
    return distribute(arr, count + 1)

print(distribute(arr, 0))
        
        
