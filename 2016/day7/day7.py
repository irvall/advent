import sys, re


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

aba = r'((\w)\w\2)'
brackets = r'(\[[^]]*\])'
outside = r'(\]|^)([^[]*)(\[|$)'

def babs(s):
    matches = re.findall(aba, s)
    return [f'{m[0][1]}{m[0][0]}{m[0][1]}' for m in matches] if matches and matches[0][0] != matches[0][1] else [0]

ans = 0
for line in lines:
    outer = re.sub(brackets, ' ', line).strip()
    inner = re.sub(outside, ' ', line).strip()
    for bab in babs(outer):
        if bab in inner:
            ans += 1
            
print(ans)

