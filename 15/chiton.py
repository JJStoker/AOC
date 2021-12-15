import math
from collections import defaultdict


INPUT_FILE = "./sample.txt" if False else "./input.txt"

risk_levels = []
with open(INPUT_FILE, "r") as input_file:
    for line in map(str.strip, input_file.readlines()):
        risk_levels.append([int(x) for x in line.strip()])

def find_shortest_path(tiles=1):
    row_dirs = [-1, 0, 1, 0]
    col_dirs = [0, 1, 0, -1]
    if tiles > 1:
        len_x = len(risk_levels[0])
        len_y = len(risk_levels)
        def get_new_risk_level(risk, d):
            for _ in range(d):
                risk += 1
                if risk > 9:
                    risk = 1
            return risk
        
        for t in range(1, tiles):
            for line in risk_levels:
                for i in range(len_x):
                    line.append(get_new_risk_level(line[i], t))
        
        len_y = len(risk_levels)
        for t in range(1, tiles):
            for i in range(len_y):
                new_line = [get_new_risk_level(value, t) for value in risk_levels[i]]
                risk_levels.append(new_line)
    
    len_x = len(risk_levels[0])
    len_y = len(risk_levels)
    risks = defaultdict(lambda: math.inf)
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
                new_risk_value = risks[(row, col)] + risk_levels[row_dir][col_dir]
                if neighbour_risk > new_risk_value:
                    risks[(row_dir, col_dir)] = new_risk_value
                    path.append((row_dir, col_dir))
    return risks[(len_x - 1, len_y - 1)]

def part_1():
    print (f'Part 1: {find_shortest_path(1)}')

def part_2():
    print(f'Part 2: {find_shortest_path(5)}')

part_1()
part_2()
