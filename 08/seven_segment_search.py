from collections import defaultdict
from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'


signal_patterns: List[List[str]] = []
with open(INPUT_FILE, 'r') as input_file:
    signal_patterns = [x.strip().split(' | ') for x in input_file.readlines()]


def part_1():
    easy_numbers = 0
    for [_, output_value] in signal_patterns:
        ez = filter(lambda x: 2 <= len(x) <= 4 or len(x) == 7, output_value.split(' '))
        easy_numbers += len(list(ez))
    print (f'Part 1: {easy_numbers}')
part_1()
