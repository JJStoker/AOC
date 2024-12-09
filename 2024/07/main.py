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
            ans, *numbers = map(int, re.findall(r'\d+', line))
            inp.append((ans, numbers))
    return inp

def check(answer, numbers, *ops):
    for op in map(iter, product([*ops], repeat = len(numbers) - 1)):
        func = lambda a, b: next(op)(a, b)
        if functools.reduce(func, numbers) == answer:
            return answer
    return 0

def part_01():
    rows = get_input()
    print(f"Day 07, part 1: {sum(check(answer, numbers, add, mul) for answer, numbers in rows)}")

def part_02():
    rows = get_input()
    concat = lambda a, b: int(str(a) + str(b))
    print(f"Day 07, part 2: {sum(check(answer, numbers, add, mul, concat) for answer, numbers in rows)}")
        

part_01()
part_02()
