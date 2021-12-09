from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'


def part_1():
    score = 0
    rows: List[List[int]] = [] 
    with open(INPUT_FILE, 'r') as input_file:
        rows = list(map(lambda xs: list(map(int, xs)), map(list, map(str.strip, input_file.readlines()))))
        
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

part_1()
