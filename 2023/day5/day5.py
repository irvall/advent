import sys, re

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def read_section(section, chunk=True):
    res = [int(_) for _ in num_reg.findall(section)]
    return chunk_list(res, 3) if chunk else res

use_test = False
if len(sys.argv) > 1:
    use_test = True
text = open('mini.txt' if use_test else 'input.txt').read()
num_reg = re.compile(r'\d+')
sections = text.split('\n\n')
seeds = read_section(sections[0], chunk=False)
chunked_sections = [read_section(sections[i]) for i in range(1, 8)]
low = sys.maxsize 
memoize = {}

for seed_start, seed_range in chunk_list(seeds, 2):
    if not seed_start in memoize: 
        for seed in range(seed_start, seed_start + seed_range):
            for sec in chunked_sections:
                for dest_start, source_start, range_len in sec:
                    if source_start <= seed < (source_start+range_len):
                        diff = dest_start - source_start 
                        seed += diff
                        memoize[seed] = seed
                        break
            if min(low, seed) < low:
                low = seed
                print(low)
            memoize[seed] = seed

print(low)
