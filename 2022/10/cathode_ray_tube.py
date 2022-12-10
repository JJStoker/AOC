import re
from collections import deque

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

def part_01():
    signal = 0
    cycle = 0
    x = 1
    for instruction in inputs:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += (cycle * x)
        cmd = instruction.split()
        if cmd[0] == "addx":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal += (cycle * x)
            x += int(cmd[1])
    
    print(f"Part 1: {signal}")

part_01()