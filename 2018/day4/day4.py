import sys, re
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Tuple

use_test = False
if len(sys.argv) > 1:
    use_test = True

lines = [_.rstrip() for _ in open('mini.txt' if use_test else 'input.txt').readlines()]

"""
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
"""

date_format = "%Y-%m-%d %H:%M"


guard_reg = re.compile(r'Guard #(\d+) begins shift')
guards = defaultdict(list[Tuple[datetime, bool]])
dates_cmd = [(line[1:17], line[19:]) for line in lines]
for date, cmd in dates_cmd:
    if 'Guard' in cmd:
        id,*_ = guard_reg.match(cmd).groups()
        continue

    parsed_date = datetime.strptime(date, date_format)
    asleep = False if 'asleep' not in cmd or 'begins' in cmd else True
    guards[id].append((parsed_date, asleep))

for k,v in guards.items():
    print()
    print(v)
    v = sorted(v, key=lambda tup: tup[0])
    print(v)
    guards[k] = v

one_minute = timedelta(minutes=1)
most_minutes = -sys.maxsize 
guards_sleep = {}
for k,v in guards.items():
    prev: datetime = None
    minutes = defaultdict(int)
    minutes_asleep = 0
    for time,asleep in v:
        if not prev: prev = time
        if not asleep and prev:
            while prev < time:
                minutes[prev.minute] += 1
                minutes_asleep += 1
                prev += one_minute
        prev = time
    if minutes_asleep >= most_minutes:
        most_minutes = minutes_asleep
    
    guards_sleep[int(k)] = (minutes_asleep, minutes)

guard_sleep = sorted(list(guards_sleep.items()), key=lambda tup: tup[1][0], reverse=True)[0]
id, minutes = guard_sleep
print(id, minutes)
minute,_ = sorted(minutes[1].items(), key=lambda tup: tup[1], reverse=True)[0]
print(minute*id)

# too high
40712
48524










        