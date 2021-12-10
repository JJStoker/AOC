from collections import defaultdict
from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'


crabs: List[int] = []
with open(INPUT_FILE, 'r') as input_file:
    crabs = [int(x) for x in input_file.read().split(',')]

def part_1():
    median = sorted(crabs)[len(crabs) // 2]
    print(f'Part 1: {sum(list(map(lambda x: abs(x - median), crabs)))}')

part_1()
