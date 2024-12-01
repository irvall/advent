from collections import defaultdict
import sys


use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]

uniques = {1,2,3, 4, 7, 8}
ans = 0

"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""

M = {
    frozenset({0,1,2,4,5,6}): 0,
    frozenset({2,5}): 1,
    frozenset({0,2,3,4,6}): 2,
    frozenset({0,2,3,5,6}): 3,
    frozenset({1,2,3,5}): 4,
    frozenset({0,1,3,5,6}): 5,
    frozenset({0,1,3,4,5,6}): 6,
    frozenset({0,2,5}): 7,
    frozenset({0,1,2,3,4,5,6}): 8,
    frozenset({0,1,2,3,5,6}): 9
}

def read_digit(truth, section):
    print('reading', section)
    digits = []
    for c in section:
        digits.append(truth[c])
    return M[frozenset(digits)]

def make_truth(sections, rev=False):
    truth = {}
    ordered = sorted(sections, key=len)
    print(ordered)
    for section in ordered:
        n = len(section)
        if n not in {2,3,4,7}: continue
        order = []
        print('\nsection', section)
        print('truth', truth)
        if n == 2:
            order = [2,5]
        elif n == 3:
            order = [0]
        elif n == 4:
            order = [3,1]
        elif n == 7:
            order = [6,4]
        if order:
            it = iter(order if not rev else reversed(order))
            for ch in section:
                if ch not in truth:
                    truth[ch] = next(it, None)
            should_be_none = next(it,None)
            assert(should_be_none == None)
                    
    return truth
                
            



for line in lines:
#for line in ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']:
    signal, output = line.split('|')
    signal_patterns = signal.strip().split()
    output_patterns = output.strip().split()
    truth = make_truth(signal_patterns)
    print('signal', signal_patterns),
    print('truth', truth)
    for s in output_patterns:
        digit = read_digit(truth, s)
        print(s, digit)
            
