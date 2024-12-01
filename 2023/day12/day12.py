lines = [line.rstrip() for line in open('input.txt', 'r').readlines()]

def arrs(springs, groups, si, gi):
    
    if si >= len(springs):
        return 1 if sum(groups) == 0 else 0

    if springs[si] == '?':


ans = 0
for line in lines:
    springs, groups = line.split()
    ans += arrs(springs, groups, 0, 0)
    

