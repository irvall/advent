import sys, re
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Tuple

use_test = False
if len(sys.argv) > 1:
    use_test = True

one_minute = timedelta(minutes=1)
lines = [_.rstrip() for _ in open('mini.txt' if use_test else 'input.txt').readlines()]
dates = []

guards = defaultdict(lambda: defaultdict(int))
id = None
asleep = False
prev_stamp = None
for line in lines:
    date, ins = [_.strip() for _ in line.split(']')]
    timestamp = datetime.fromisoformat(date[1:])
    if ins.startswith('Guard'):
        id = ins.split()[1]
        prev_stamp = timestamp
    if asleep and ins.startswith('wakes'):
        asleep = False
        current_time = datetime.fromisoformat(date[1:])
        while prev_stamp != current_time:
            guards[id][prev_stamp.minute] += 1
            prev_stamp += one_minute
    if ins.startswith('falls'):
        asleep = True
        prev_stamp = timestamp


guard_to_use = None
most_mins = 0
for guard, freq in guards.items():
    minutes_slept = sum([count for _,count in freq.items()])
    if minutes_slept > most_mins:
        guard_to_use = guard
        most_mins = minutes_slept
   


record_count, record_minute = 0, 0
values = guards[guard_to_use].items()
for minute, count in values:
    if count > record_count:
        record_minute = minute
        record_count = count
print(int(guard_to_use[1:]) * record_minute)
        
            

   
# sleeps_from = datetime.fromisoformat('1518-01-23 00:19')
# sleeps_to = datetime.fromisoformat('1518-05-03 00:43')
# print('sleeps from', sleeps_from)
# print('sleeps to', sleeps_to)
# while sleeps_from != sleeps_to:
#     print(sleeps_from.minute)
#     sleeps_from += one_minute
    



    
    






        