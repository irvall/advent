import sys


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

"""
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.

"""

table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

table2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

start_to_end = {'(': ')', '{': '}', '[': ']', '<': '>'}
end_to_start = {v: k for k, v in start_to_end.items()}
def is_valid(s):
    stack = []
    illegal_char = None
    for c in s:
        if c in start_to_end:
            stack.append(c)
            continue
        = end_to_start[c]
        if stack.pop() != matching:
            illegal_char = c
            break
    return (table[illegal_char], stack) if illegal_char else (0, stack)
   
def repair(s):
    v, stack = is_valid(s)
    if v > 0:
        return 0
    fixed = reversed([start_to_end[c] for c in stack])  
    score = 0
    for c in fixed:
        score *= 5
        score += table2[c]
    return score

        
        
    

scores = []
for line in lines:
    s = repair(line)
    if s: scores.append(s)
scores = sorted(scores)
print(scores[len(scores)//2])
    
