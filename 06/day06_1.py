from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'x y')

with open('input.txt') as f:
    data = f.readlines()

coordinates = {}
for line in data:
    x, y = line.split(',')
    coordinates[Coordinate(int(x), int(y))] = []

min_x = min(coordinates, key=lambda c: c.x).x - 1
min_y = min(coordinates, key=lambda c: c.y).y - 1

max_x = max(coordinates, key=lambda c: c.x).x + 1
max_y = max(coordinates, key=lambda c: c.y).y + 1

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        grid_coord = Coordinate(x, y)

        nearest_distance = float('+inf')
        nearest_coords = []
        for coord in coordinates:
            distance = abs(grid_coord.x - coord.x) + abs(grid_coord.y - coord.y)
            if distance == nearest_distance:
                nearest_coords.append(coord)
            elif distance < nearest_distance:
                nearest_distance = distance
                nearest_coords = [coord]

        if len(nearest_coords) == 1:
            nearest = nearest_coords[0]
            coordinates[nearest].append(grid_coord)


def coord_area(coord):
    area = 0
    for c in coordinates[coord]:
        if c.x <= min_x or c.y <= min_y or c.x >= max_x or c.y >= max_y:
            area += float('+inf')
        else:
            area += 1
    return area


max_area = 0
max_coord = None
for coord in coordinates:
    area = coord_area(coord)
    if area > max_area and area < float('+inf'):
        max_area = area
        max_coord = coord

print(max_area)
