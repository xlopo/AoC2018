from collections import Counter
import re
from dataclasses import dataclass

@dataclass()
class Entity(object):
    id: int
    x_offset: int
    y_offset: int
    width: int
    height: int

    @staticmethod
    def new(id, x_offset, y_offset, width, height):
        return Entity(int(id), int(x_offset), int(y_offset), int(width), int(height))

    def tiles(self):
        for x in range(self.width):
            for y in range(self.height):
                yield (self.x_offset+x, self.y_offset+y,)




with open('input') as f:
    data = f.read()

prog = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', re.MULTILINE)

entities = [Entity.new(*e) for e in prog.findall(data)]



tiles = []

for e in entities:
    for tile in e.tiles():
        tiles.append(tile)

count = Counter(tiles)
print(len(list(filter(lambda x: x > 1, count.values()))))

for e in entities:
    counts = {count[t] for t in e.tiles()}
    if counts == {1}:
        print(e)
        break

