with open('input') as f:
    lines = f.readlines()

changes = [int(l) for l in lines]

seen = set()

frequency = 0

change_iter = iter(changes)
while True:
    if frequency in seen:
        break

    seen.add(frequency)
    try:
        i = next(change_iter)
    except StopIteration:
        change_iter = iter(changes)
        i = next(change_iter)

    frequency += i

print(frequency)
