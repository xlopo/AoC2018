from collections import namedtuple


class Coordinate(namedtuple('Coordinate', 'x y')):
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


with open('input.txt') as f:
    data = f.readlines()

coordinates = {}
for line in data:
    y, x = line.split(',')
    coordinates[Coordinate(int(x), int(y))] = []

min_x = min(coordinates, key=lambda c: c.x).x - 1
min_y = min(coordinates, key=lambda c: c.y).y - 1

max_x = max(coordinates, key=lambda c: c.x).x + 1
max_y = max(coordinates, key=lambda c: c.y).y + 1

region = []
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        grid_coord = Coordinate(x, y)

        distances = []
        distances = [c.distance(grid_coord) for c in coordinates]

        s = sum(distances)
        # print(grid_coord, ':', s, '|', *distances, sep=' ')

        if sum(distances) < 10000:
            region.append(grid_coord)

print(len(region))
