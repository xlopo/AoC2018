from collections import Counter
import re
from datetime import datetime, timedelta

with open('input') as f:
    data = sorted(f.readlines())

guard_log = []
guards = set()

guard_id = None
sleep_ts = None
wake_ts = None

for line in data:
    m = re.search(r'\[(.*?)\] Guard #(\d+) begins shift', line)
    if m is not None:
        guard_id = int(m.group(2))
        guards.add(guard_id)
        continue

    m = re.search(r'\[(.*?)\] falls asleep', line)
    if m is not None:
        sleep_ts = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
        continue

    m = re.search(r'\[(.*?)\] wakes up', line)
    if m is not None:
        wake_ts = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
        minute = timedelta(minutes=1)

        ts = sleep_ts
        while ts < wake_ts:
            if ts.hour == 0:
                guard_log.append((guard_id, ts.minute,))
            ts += minute
        continue

    raise ValueError(line)


count = Counter(guard_log)
most_slept_minute = count.most_common(1)[0][0]

print(most_slept_minute[0] * most_slept_minute[1])

