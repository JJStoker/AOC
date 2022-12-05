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


def part_2():
    count = 0
    for (mI, m) in enumerate(rows):
        if mI < 3: continue
        prev_sum = rows[mI - 1] + rows[mI - 2] + rows[mI - 3]
        curr_sum = m + rows[mI - 1] + rows[mI - 2]
        if curr_sum > prev_sum:
            count += 1
    print(f'Part 2: {count}')

part_1()
part_2()
