from collections import defaultdict
from typing import List, Tuple

INPUT_FILE = './sample.txt' if False else './input.txt'


byte_list: List[str] = []
with open(INPUT_FILE, 'r') as input_file:
    byte_list = list(map(str.strip, input_file.readlines()))
    
    
def part_1():
    ones = defaultdict(int)
    byte_cnt = len(byte_list)
    gamma = ''
    epsilon = ''
    for bY in byte_list:
        for (c, b) in enumerate(list(bY)):
            if b == '1':
                ones[c] += 1
    for key in sorted(ones.keys()):
        gamma += f'{1 if ones[key] >= (byte_cnt / 2) else 0}'
        epsilon += f'{0 if ones[key] >= (byte_cnt / 2) else 1}'
    print (f'Part 1: {int(gamma, 2) * int(epsilon, 2)}')

part_1()
