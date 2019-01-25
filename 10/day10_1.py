import re
from dataclasses import dataclass
import time
import math

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


prog = re.compile(r'position=<(.+?),(.+?)> velocity=<(.+?),(.+?)>')
with open('input.txt.example') as f:
    points = [Point(px, py, vx, vy) for px, py, vx, vy in prog.findall(f.read())]


def print_grid(grid, pretty=False):
    for line in grid:
        if pretty:
            print(''.join(['.' if z == 0 else '#' for z in line]))
        else:
            print(''.join([str(z) for z in line]))
    print()


second = 0
sizes = []
while True:
    min = Coordinate(points[0].pos.x, points[0].pos.y)
    max = Coordinate(min.x, min.y)

    for p in points:
        if p.pos.x < min.x:
            min.x = p.pos.x
        if p.pos.y < min.y:
            min.y = p.pos.y
        if p.pos.x > max.x:
            max.x = p.pos.x
        if p.pos.y > max.y:
            max.y = p.pos.y

    size = Coordinate(abs(min.x) + abs(max.x), abs(min.y) + abs(max.y))
    grid = [[0]*(size.x+1) for z in range(size.y+1)]
    focal_sum = [[0]*(size.x+1) for z in range(size.y+1)]

    for p in points:
        x = p.pos.x + min.x
        y = p.pos.y + min.y

        grid[y][x] = 1

    for y in range(size.y+1):
        for x in range(size.x+1):
            s = 0
            if y-1 >= 0:
                if x-1 >= 0:
                    s += grid[y-1][x-1]
                s += grid[y-1][x]
                if x+1 <= size.x:
                    s += grid[y-1][x+1]

            if x-1 >= 0:
                s += grid[y][x-1]
            s += grid[y][x]
            if x+1 <= size.x:
                s += grid[y][x+1]

            if y+1 <= size.y:
                if x-1 >= 0:
                    s += grid[y+1][x-1]
                s += grid[y+1][x]
                if x+1 <= size.x:
                    s += grid[y+1][x+1]

            focal_sum[y][x] = s

    # print(min,  max)


    # size = pow(abs(min.x) + abs(max.x),2) + pow(abs(min.y) + abs(max.y),2)
    # size = Coordinate(abs(min.x) + abs(max.x), abs(min.y) + abs(max.y))
    # print(f'second={second}', f'size={size}')
    # print(size)
    sizes.append(size)
    # if size == 130:
    #     print(f'second={second}')
    #     for y in range(abs(min.y) + abs(max.y) + 1):
    #         for x in range(abs(min.x) + abs(max.x) + 1):
    #             coord = Coordinate(x + min.x, y + min.y)
    #             match = False
    #             for p in points:
    #                 if p.pos == coord:
    #                     # print(coord, p)
    #                     # print('match!!!!')
    #                     match = True
    #             if match:
    #                 print('#', end='')
    #             else:
    #                 print('.', end='')
    #         print()
    #     print()

    s = 0
    for row in focal_sum:
        for col in row:
            s += col



    print(s)
    print(1 + math.log(s))
    num_coords = size.x * size.y
    odds = 1/num_coords * 1/(num_coords-1) * 1/(num_coords-2) * 1/(num_coords-3) * 1/(num_coords-4)
    print(size, num_coords, odds)

    print_grid(grid, pretty=True)
    print_grid(focal_sum, pretty=False)

    # time.sleep(1)

    second += 1
    for p in points:
        p.pos = p.pos + p.v

    if second > 3:
        break

sizes = sorted(sizes)[0:10]
print(sizes)