import os
import time
from collections import defaultdict
from typing import DefaultDict, List, Tuple

INPUT_FILE = './sample.txt' if False else './input.txt'

grid = defaultdict(int)
print(grid)
with open(INPUT_FILE, 'r') as input_file:
    for (rI, row) in enumerate(map(str.strip, input_file.readlines())):
        for (cI, val) in enumerate(list(row)):
            grid[(rI, cI)] = int(val)

print(grid)

def dump_grid():
    os.system('clear')
    for x in range(10):
        print(f'{"".join(map(str, [grid[(x, y)] for y in range(10)]))}', end="\n")
    time.sleep(0.01)

def part_1(steps=100):
    # l     = x - 1 y = 0
    # dtl   = x - 1 y + 1
    # t     = x = 0 y + 1
    # dtr   = x + 1 y + 1
    # r     = x + 1 y = 0
    # dbr   = x + 1 y - 1
    # b     = x = 0 y - 1
    # dbl   = x - 1 y - 1
    d_x_map = [-1, -1, 0, 1, 1, 1, 0, -1]
    d_y_map = [0, 1, 1, 1, 0, -1, -1, -1]
    count = 0
    for i in range(steps):
        flashes = []
        for (rI, cI) in grid:
            grid[(rI, cI)] += 1
        for (rI, cI) in grid:
            if grid[(rI, cI)] == 10:
                flashes.append((rI, cI))
        while len(flashes):
            (x1, y1) = flashes.pop(0)
            if grid[(x1, y1)] == -1: continue
            grid[(x1, y1)] = -1
            count += 1
            for d in range(8):
                rx = x1 + d_x_map[d]
                ry = y1 + d_y_map[d]
                if (
                    0 <= rx < 10 and
                    0 <= ry < 10 and
                    grid[(rx, ry)] != -1
                ):
                    grid[(rx, ry)] += 1
                    if grid[(rx, ry)] >= 10:
                        flashes.append((rx, ry))
        for (rI, cI) in grid:
            if grid[(rI, cI)] == -1:
                grid[(rI, cI)] = 0
        dump_grid()
    print(f'Part 1: {count}')

part_1()
