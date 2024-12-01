strs = open('input.txt', 'r').read().split(',')
def h(s):
    r = 0
    for c in s:
        o = ord(c)
        r += o
        r *= 17
        r %= 256
    return r

print(sum((h(_) for _ in strs)))
