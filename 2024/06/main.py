import os
from collections import defaultdict, deque, OrderedDict

DEBUG = os.getenv("DEBUG", "off").lower() == "on"

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def get_input(sample_filename=None):
    input = []
    initial_position = (0, 0)
    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        for line in i.readlines():
            if line == "\n":
                continue
            row = list(line.strip())
            for d in directions.keys():
                if d in row:
                    initial_position = (len(input), row.index(d), )
            input.append(row)
    return input, initial_position

def part_01():
    grid, initial_position = get_input()
    traversed = { initial_position }
    heading = grid[initial_position[0]][initial_position[1]]
    y, x = initial_position
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        dy, dx = directions[heading]
        ny, nx = y + dy, x + dx
        if (
            ny >= len(grid)
            or nx >= len(grid[0])
            or ny < 0
            or nx < 0
        ):
            break
        if grid[ny][nx] == '#':
            heading = right_turn[heading]
        else:
            traversed.add((ny, nx))
            x, y = nx, ny
    print(f"Day 06, part 1: {len(traversed)}")

def part_02():
    grid, initial_position = get_input()
    total = 0
    print(f"Day 06, part 1: {total}")

part_01()
part_02()
