import os
import re
import functools
from itertools import product
from operator import add, mul

DEBUG = os.getenv("DEBUG", "off").lower() == "on"

def get_input(sample_filename=None):
    inp = []
    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        for line in i.readlines():
            groups = re.findall(r'([L|R])(\d+)', line)
            inp.append((groups[0][0], int(groups[0][1])))
    return inp

def part_01():
    rows = get_input()
    pos = 50
    times = 0
    for dir, clicks in rows:
        new_pos = pos + (clicks * (1 if dir == 'R' else -1))
        pos = new_pos % 100
        if pos == 0:
            times += 1
        
    print(f"Day 01, part 1: {times}")

def part_02():
    rows = get_input()
    pos = 50
    times = 0
    for dir, clicks in rows:
        new_pos = pos + (clicks * (1 if dir == 'R' else -1))
        if dir == 'R':
            rotations = new_pos // 100
        else:
            rotations = (pos - 1) // 100 - (new_pos - 1) // 100
        pos = new_pos % 100
        times += rotations

    print(f"Day 01, part 2: {times}")   

part_01()
part_02()
