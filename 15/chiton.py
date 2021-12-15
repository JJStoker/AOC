import math
from collections import defaultdict


INPUT_FILE = "./sample.txt" if False else "./input.txt"

risk_levels = defaultdict(int)
with open(INPUT_FILE, "r") as input_file:
    for y, line in enumerate(map(str.strip, input_file.readlines())):
        for x in range(len(line)):
            risk_levels[tuple(map(int, (x, y)))] = int(line[x])
            
def part_1():
    row_dirs = [-1, 0, 1, 0]
    col_dirs = [0, 1, 0, -1]
    len_x = len_y = int(math.sqrt(len(risk_levels)))
    risks = defaultdict()
    for (x, y) in risk_levels:
        risks[(x, y)] = 999999
    risks[(0,0)] = 0
    path = [(0, 0)]
    while path:
        (row, col) = path.pop(0)
        for d in range(4):
            row_dir = row + row_dirs[d]
            col_dir = col + col_dirs[d]            
            if (
                (0 <= row_dir < len_x) and
                (0 <= col_dir < len_y)
            ):
                neighbour_risk = risks[(row_dir, col_dir)]
                new_risk_value = risks[(row, col)] + risk_levels[(row_dir, col_dir)]
                if neighbour_risk > new_risk_value:
                    risks[(row_dir, col_dir)] = new_risk_value
                    path.append((row_dir, col_dir))
    print (f'Part 1: {risks[(len_x - 1, len_y - 1)]}')

part_1()
