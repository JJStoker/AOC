from typing import List, Tuple

INPUT_FILE = './sample.txt' if False else './input.txt'


instructions: List[Tuple[str, int]] = []
with open(INPUT_FILE, 'r') as input_file:
    instructions = list(map(
        lambda cmd_unit: (cmd_unit[0], int(cmd_unit[1])),
        map(str.split, map(str.strip, input_file.readlines()))
    ))

    
def part_01():
    y, x = 0, 0
    for (command, units) in instructions:
        if command == 'forward':
            x += units
        elif command == 'up':
            y -= units
        elif command == 'down':
            y += units
    print(f'Part 1: {x * y}')

part_01()
