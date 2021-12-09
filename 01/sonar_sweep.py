from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'

rows: List[int] = []
with open(INPUT_FILE, 'r') as input_file:
    rows = list(map(int, map(str.strip, input_file.readlines())))
                
def part_1():
    count = 0
    curr = rows[0]
    for measurement in rows:
        if measurement > curr:
            count += 1
        curr = measurement
        
    print(f'Part 1: {count}')

part_1()
