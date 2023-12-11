import functools
import math
nums = [int(_.rstrip()) for _ in open('mini.txt').readlines()]
x = functools.reduce(math.lcm, nums)
print(x)

def find_golden_number(numbers, target):
    n = len(numbers)
    
    # Create a 2D table to store the results of subproblems
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
    
    # Base case: subset with a sum of 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # If the current number is greater than the target, it can't be included
            if numbers[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Either include the current number or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]
    
    # If the target is achievable, find the combination of numbers
    if dp[n][target]:
        result = []
        i, j = n, target
        while i > 0 and j > 0:
            if dp[i][j] and not dp[i - 1][j]:
                result.append(numbers[i - 1])
                j -= numbers[i - 1]
            i -= 1
        return result[::-1]
    else:
        return None

# Example usage:
numbers = nums
target = 20
golden_numbers = find_golden_number(numbers, target)
print(golden_numbers)