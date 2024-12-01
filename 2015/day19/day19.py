from collections import defaultdict
import sys


use_test = len(sys.argv) == 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

def indices(s, search):
    n = len(s)
    def inner(i, res):
        if i >= n: return res
        next_occurence = s[i:].find(search)
        if next_occurence == -1:
            return res
        res.append(next_occurence + i)
        return inner(i + next_occurence + 1, res)
    return inner(0, [])

"""
H => HO
H => OH
O => HH
"""
molecule = 'HOH'
#seed = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
strings = set()
mappings = defaultdict(list)

for line in lines:
    target, replacement = line.split(' => ')
    mappings[target].append(replacement)


print(mappings)


def replace(seed, target, replacement): 
    m = len(target)
    matches = indices(seed, target)
    res = []
    for idx in matches:
        s = seed[0:idx] + replacement + seed[idx + m:]
        res.append(s)
    return res

seen = set()

def step(seed, target, replacement, res):
    print(f'\nstep({seed}, {target}, {replacement})')
    if seed == molecule:
        return res
    targets = replace(seed, target, replacement)
    print('targets', targets)
    for target in targets:
        for target_ch in target:
            if target_ch in seen:
                continue
            seen.add(target_ch)
            ms = mappings[target_ch]
            for new_seed in ms:
                for seed_char in new_seed:
                    return step(new_seed, seed_char, target_ch, res + 1)
    return res
            
        
"""
In [29]: replace('e', 'e', 'O')
Out[29]: ['O']

In [30]: mappings['O']
Out[30]: ['HH']

In [31]: replace('HH', 'H', 'O')
Out[31]: ['OH', 'HO']

In [32]: replace('OH', 'O', 'OH')
Out[32]: ['OHH']

In [33]: replace('OH', 'O', 'HO')
Out[33]: ['HOH']
"""
step('e', 'e', 'O', 0)
