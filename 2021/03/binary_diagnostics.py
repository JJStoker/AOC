from collections import defaultdict
from typing import List

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

def part_2():
    oxygen = list(byte_list)
    co2_scrubber = list(byte_list)
    for i in range(len(byte_list[0])):
        if len(oxygen) > 1:
            o0 = [x for x in oxygen if x[i] == '0']
            o1 = [x for x in oxygen if x[i] == '1']
            oxygen = o1 if len(o1) >= len(o0) else o0
        if len(co2_scrubber) > 1:
            o0 = [x for x in co2_scrubber if x[i] == '0']
            o1 = [x for x in co2_scrubber if x[i] == '1']
            co2_scrubber = o0 if len(o1) >= len(o0) else o1
    print (f'Part 2: {int(oxygen[0], 2) * int(co2_scrubber[0], 2)}')

part_1()
part_2()
