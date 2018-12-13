from collections import Counter

with open('input') as f:
    lines = f.readlines()

counts = [Counter(line) for line in lines]

twos = list(filter(lambda x: 2 in x.values(), counts))
print(len(twos))

threes = list(filter(lambda x: 3 in x.values(), counts))
print(len(threes))

checksum = len(twos) * len(threes)
print(checksum)