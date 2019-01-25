import re
from dataclasses import dataclass
from collections import Counter

@dataclass(order=True)
class Coordinate:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


@dataclass(order=True)
class Point:
    pos: Coordinate
    v: Coordinate

    def __init__(self, px, py, vx, vy):
        self.pos = Coordinate(px, py)
        self.v = Coordinate(vx, vy)

    def update(self):
        self.pos.x += self.v.x
        self.pos.y += self.v.y


def print_grid(points):
    min_y = min(points, key=lambda x: x.pos.y).pos.y
    max_y = max(points, key=lambda x: x.pos.y).pos.y
    min_x = min(points, key=lambda x: x.pos.x).pos.x
    max_x = max(points, key=lambda x: x.pos.x).pos.x

    coords = [point.pos for point in points]

    y = min_y
    while y < max_y + 1:
        x = min_x
        while x < max_x + 1:
            p = Coordinate(x, y)
            if p in coords:
                print('#', end='')
            else:
                print('.', end='')
            x += 1
        y += 1
        print()


def count_lines(points):
    coords = {(point.pos.x, point.pos.y) for point in points}
    min_y = min(coords, key=lambda c: c[1])[1]
    max_y = max(coords, key=lambda c: c[1])[1]

    counts = []
    for c in coords:
        x, y = c
        if y > min_y:
            continue

        count = 0
        while y < max_y + 1:
            if (x, y) in coords:
                count += 1
            else:
                break
            y += 1

        counts.append(count)
    counts = Counter(counts)
    max_length = max(counts.keys())
    return max_length, counts[max_length]


prog = re.compile(r'position=<(.+?),(.+?)> velocity=<(.+?),(.+?)>')
with open('input.txt') as f:
    points = [Point(px, py, vx, vy) for px, py, vx, vy in prog.findall(f.read())]

second = 0
while True:
    count = count_lines(points)
    if count[0] >= 5:
        print_grid(points)
        print(f'second={second}, lines={count}')
        print()
        break

    for p in points:
        p.update()
