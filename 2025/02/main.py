import os
import re
import functools
from itertools import product
from operator import add, mul

DEBUG = os.getenv("DEBUG", "off").lower() == "on"

def get_input(sample_filename=None):
    inp = []
    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        inp.extend(map(str.strip, i.read().strip().split(',')))
    return inp

def part_01():
    rows = get_input()
    r = []
    for ids in rows:
        id1, id2 = map(int, ids.split('-'))
        
        for n in range(id1, id2 + 1):
            if len(str(n)) % 2 != 0:
                continue
            
            sn = str(n)
            half = len(sn) // 2
            if sn[0:half] == sn[half:len(sn)]:
                r.append(n)
    print(f"Day 02, part 1: {sum(r)}")

def part_02():
    rows = get_input()
    times = 0
    print(f"Day 02, part 2: {times}")   

part_01()
part_02()
