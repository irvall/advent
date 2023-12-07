import sys, re
from datetime import datetime
from collections import defaultdict

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
guards = defaultdict(list)
dates_cmd = [(line[1:17], line[19:]) for line in lines]
id = -1
for date, cmd in dates_cmd:
    if 'Guard' in cmd:
        id,*_ = guard_reg.match(cmd).groups()
        continue

    parsed_date = datetime.strptime(date, date_format)
    guards[id].append((parsed_date, True if 'asleep' in cmd else False))

for k,v in guards.items():
    v.sort(key=lambda tup: tup[0])

def guard_sleeps(dates):
    ans = 0
    sleeping = False
    last_timestamp = None
    for date, asleep in dates:
        sleeping = asleep
        if not last_timestamp:
            last_timestamp = date
        span = date - last_timestamp
        if span.total_seconds() > 80000:
            continue
        if not asleep:
            ans += span.total_seconds() / 60
    return ans
    
    




for k,v in guards.items():
    print(k,v)
    print(guard_sleeps(v))
# todo sort by timestamp
