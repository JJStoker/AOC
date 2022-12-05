from collections import deque
from functools import reduce
from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'


rows: List[List[int]] = [] 
with open(INPUT_FILE, 'r') as input_file:
    rows = list(map(lambda xs: list(map(int, xs)), map(list, map(str.strip, input_file.readlines()))))

def part_1():
    score = 0
    for (rI, row) in enumerate(rows):
        for (cI, col) in enumerate(row):
            if (
                (rI == 0                or col < rows[rI - 1][cI]) and 
                (rI == len(rows) - 1    or col < rows[rI + 1][cI]) and 
                (cI == 0                or col < rows[rI][cI - 1]) and 
                (cI == len(row) - 1     or col < rows[rI][cI + 1])
            ):
                score += (col + 1)
    print(f'Part 1: {score}')


def part_2():
    row_dirs = [-1, 0, 1, 0]
    col_dirs = [0, 1, 0, -1]
    # Breadth-first search: https://en.wikipedia.org/wiki/Breadth-first_search
    basin_sizes: List[int] = []
    handled = set()
    for rI in range(len(rows)):
        for cI in range(len(rows[0])):
            if (rI, cI) not in handled and rows[rI][cI] != 9:
                size = 0
                basin = deque()
                basin.append((rI, cI))
                while basin:
                    (row, col) = basin.popleft()
                    if (row, col) in handled:
                        continue
                    handled.add((row, col))
                    size += 1
                    for d in range(4):
                        row_dir = row + row_dirs[d]
                        col_dir = col + col_dirs[d]
                        if (
                            (0 <= row_dir < len(rows) - 1) and
                            (0 <= col_dir < len(rows[0]) - 1) and
                            rows[row_dir][col_dir] != 9
                        ):
                            basin.append((row_dir, col_dir))
                basin_sizes.append(size)
    print(f'Part 2: {reduce(lambda a, b: a * b, sorted(basin_sizes)[-3:])}')

part_1()
part_2()
