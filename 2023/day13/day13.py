test = True
sections = [section.split('\n') for section in open('mini.txt' if test else 'input.txt', 'r').read().split('\n\n')]
sections_90 = []

def pp(section):
    for row in section:
        print(row)
    print()

def rotate(section):
    rotated = []
    for y in range(len(section[0])):
        row = []
        for x in range(len(section)):
            row.append(section[x][y])
        rotated.append(''.join(row))
    return rotated

for s in sections:
    sections_90.append(rotate(s))

def reflection(section):
    best = 0
    idx = None
    for i in range(0, len(section)):
        j = i
        k = i
        symmetries = 0
        while j >= 0 and k < len(section) and section[j] == section[k]:
            print(j, k)
            print(section[j], section[k])
            k += 1
            j -= 1
            symmetries += 1
        if symmetries > best:
            best = symmetries
            idx = i

    if idx: return idx


ans = 0
for sec, sec90 in zip(sections, sections_90):
    a = reflection(sec)
    if a:
        ans += a*100
        continue
    b = reflection(sec90)
    if b:
        ans += b
        continue
    assert False, "Wow, buddy, we should not arrive here"

print(ans)



## too low
15421
16213

# incorrect
20908
23581
26931
27634
27327
32501

## too high
32803

## not tried
