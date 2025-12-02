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
    r = []

    for id1, id2 in [
        map(int, ids.split('-'))
        for ids in rows
    ]:
        for n in range(id1, id2 + 1):
            sn = str(n)
            length = len(sn)

            for pow in range(2, length + 1):
                if length % pow != 0:
                    continue

                part_len = length // pow
                parts = [
                    sn[i * part_len : (i + 1) * part_len]
                    for i in range(pow)
                ]
                if all(p == parts[0] for p in parts):
                    r.append(n)
                    break

    print(f"Day 02, part 2: {sum(r)}")   

part_01()
part_02()
