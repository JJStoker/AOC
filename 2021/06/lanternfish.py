from collections import defaultdict
from typing import List

INPUT_FILE = './sample.txt' if False else './input.txt'


fish: List[int] = []
with open(INPUT_FILE, 'r') as input_file:
    fish = [int(x) for x in input_file.read().split(',')]

def part_1(day: str, days: int):
    fish_state = defaultdict(int)
    for f in fish:
        fish_state[f] += 1    
    for _ in range(days):
        day_state = defaultdict(int)
        for (cycle, count) in fish_state.items():
            if cycle == 0:
                day_state[6] += count
                day_state[8] += count
            else:
                day_state[cycle - 1] += count
        fish_state = day_state
    print(f'Part {day}: {sum(fish_state.values())}')

part_1('1', 80)
part_1('2', 256)
