import sys, re

use_test_data = len(sys.argv) > 1
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]
numbers = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

def part_one():
    ans = 0
    for line in lines:
        nums = re.sub('[a-z]', '', line)
        ans += int(nums[0] + nums[-1]) 
    return ans


def findall(pat, str):
    return [m.start() for m in re.finditer(pat, str)]

def part_two(): 
    ans = 0
    for line in lines:
        print()
        print(line)
        for k,v in numbers.items():
            occs = findall(k, line)
            if occs:
                i, j = occs[0], occs[-1]
                if len(occs) == 1:
                   line =  line[0:i+1] + str(v) + line[i+1:]
                else: line = line[0:i+1] + str(v) + line[i+1:j] + str(v) + line[j:]
        print(line)
        nums = re.sub('[a-z]', '', line)
        new_num = nums[0] + nums[-1]
        ans += int(new_num) 
    return ans
   
print(part_two())