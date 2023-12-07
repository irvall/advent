import functools
file = open('input.txt', 'r')
times = [int(_) for _ in file.readline().rstrip()[11:].split()]
distances = [int(_) for _ in file.readline().rstrip()[11:].split()]

def calc(record, charge_time):
    time_spent = record - charge_time
    return time_spent * charge_time

ans = 1
for record_time, distance in zip(times, distances):
    ways = 0
    for i in range(1, record_time):
        new_dist = calc(record_time, i)
        if distance < new_dist:
            ways += 1
    if ways: ans *= ways
print(ans)


