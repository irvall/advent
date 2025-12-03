import sys

use_test = len(sys.argv) > 1
file_name = "input.txt" if not use_test else "test.txt"
lines = [[c for c in _.rstrip()] for _ in open(file_name, "r")]
inf = 10e9

def find_num(s: str, take=12):
    digits = ''
    n = len(s)
    seen = set()
    last_pos = -1
    while len(digits) < take:
        idx, best = None, -inf
        for i in range(last_pos + 1, n):
            if i in seen: continue
            valid_pick = n - i >= take-len(digits)
            if valid_pick and int(s[i]) > best:
                idx, best = i, int(s[i])
        last_pos = idx
        seen.add(idx)
        digits += str(best)
    return int(digits)

print(sum(find_num(line) for line in lines))