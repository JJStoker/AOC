import os
import time
from collections import defaultdict
from typing import DefaultDict, List, Tuple

INPUT_FILE = "./sample.txt" if False else "./input.txt"
TIME_DELAY = 0.1

grid = defaultdict(int)
with open(INPUT_FILE, "r") as input_file:
    for (rI, row) in enumerate(map(str.strip, input_file.readlines())):
        for (cI, val) in enumerate(list(row)):
            grid[(rI, cI)] = int(val)


def dump_grid(step, count):
    os.system("clear")
    print(f"STEP: {step} COUNT: {count}", end="\n")
    for x in range(10):
        print(
            "".join(
                map(
                    lambda x: f'{"■" if x == 0 else "□"}',
                    [grid[(x, y)] for y in range(10)],
                )
            ),
            end="\n",
        )
    time.sleep(TIME_DELAY)


def cavern_sim():
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
    part_1, count = 0, 0
    step = 0
    while True:
        step += 1
        flashes = []
        for (rI, cI) in grid:
            grid[(rI, cI)] += 1
        for (rI, cI) in grid:
            if grid[(rI, cI)] == 10:
                flashes.append((rI, cI))
        while len(flashes):
            (x1, y1) = flashes.pop(0)
            if grid[(x1, y1)] == -1:
                continue
            grid[(x1, y1)] = -1
            count += 1
            for d in range(8):
                rx = x1 + d_x_map[d]
                ry = y1 + d_y_map[d]
                if 0 <= rx < 10 and 0 <= ry < 10 and grid[(rx, ry)] != -1:
                    grid[(rx, ry)] += 1
                    if grid[(rx, ry)] >= 10:
                        flashes.append((rx, ry))
        done = True
        for (rI, cI) in grid:
            if grid[(rI, cI)] == -1:
                grid[(rI, cI)] = 0
            else:
                done = False
        if step == 100:
            part_1 = count
        dump_grid(step, count)
        if done:
            break
    print(f"Part 1: {part_1}")
    print(f"Part 2: {step}")


cavern_sim()
