from collections import Counter
import re

with open('input') as f:
    data = f.read()

prog = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', re.MULTILINE)

tiles = []

for entry in prog.findall(data):
    entry_id, x_offset, y_offset, width, height = entry
    x_offset = int(x_offset)
    y_offset = int(y_offset)
    width = int(width)
    height = int(height)

    for x in range(width):
        for y in range(height):
            tiles.append((x_offset+x, y_offset+y))

count = Counter(tiles)
print(len(list(filter(lambda x: x > 1, count.values()))))
