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

def part_2():
    scores = 0
    ez_len_map = {2: 1, 3: 7, 4: 4, 7: 8}
    
    for [signal_pattern, output_value] in signal_patterns:
        output_to_num = defaultdict(int)
        num_to_output = [''] * 10
        signals = ["".join(sorted(signal)) for signal in signal_pattern.split()]
        outputs = ["".join(sorted(output)) for output in output_value.split()]
        for segment in signals:
            if len(segment) not in ez_len_map: continue
            output_to_num[segment] = ez_len_map[len(segment)]
            num_to_output[ez_len_map[len(segment)]] = segment
        for segment in signals:
            if len(segment) == 6: # could be either 0, 6 or 9
                less_than_7 = len(set(segment) - set(num_to_output[7]))
                less_than_4 = len(set(segment) - set(num_to_output[4]))
                if less_than_7 == 4:
                    output_to_num[segment] = 6
                elif less_than_7 == 3 and less_than_4 == 2:
                    output_to_num[segment] = 9
                else:
                    output_to_num[segment] = 0
            elif len(segment) == 5: # could be either 2, 3 or 5
                more_than_4 = len(set(segment + num_to_output[4]))
                more_than_7 = len(set(segment + num_to_output[7]))
                if more_than_4 == 7:
                    output_to_num[segment] = 2
                elif more_than_4 == 6 and more_than_7 == 6:
                    output_to_num[segment] = 5
                else:
                    output_to_num[segment] = 3
        scores += int("".join([str(output_to_num[output]) for output in outputs]))
    print (f'Part 2: {scores}')

part_1()
part_2()
