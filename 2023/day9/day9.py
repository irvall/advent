nums = [[int(digit) for digit in _.rstrip().split()] for _ in open('input.txt', 'r')]

def diff(row):
    diffs = []
    for i in range(1, len(row)):
        diffs.append(row[i]-row[i-1])
    return diffs

def all_zero(row):
    for e in row:
        if e != 0: return False
    return True

p1, p2 = 0, 0
for row in nums:
    seqs = []
    while not all_zero(row):
        seqs.append(row)
        row = diff(row)
    n = len(seqs)
    for i in range(n - 1):
        source_seq = seqs[n - i - 1]
        target_seq = seqs[n - i - 2]
        entry1 = target_seq[0] - source_seq[0] 
        entry2 = target_seq[-1] + source_seq[-1] 
        target_seq.insert(0, entry1)
        target_seq.append(entry2)
    p1 += seqs[0][-1]
    p2 += seqs[0][0]

print(p1, p2)



