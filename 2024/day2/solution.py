import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

def is_safe(nums):
    incr = nums[0] < nums[-1]
    p = nums[0]
    for i in range(1, len(nums)):
        v = nums[i]
        d = v - p
        if not (1 <= d <= 3 if incr else -3 <= d <= -1):
            return False
        p = v
    return True

def remove_index(nums, idx):
    return nums[:idx] + nums[idx + 1:]

def is_safe_perm(nums):
    for i in range(len(nums)):
        sub = remove_index(nums, i)
        if is_safe(sub): return True
    return False
        
ans = 0
for line in lines:
    nums = [int(_) for _ in line.split()]
    ans += 1 if is_safe(nums) or is_safe_perm(nums) else 0
print(ans) 
