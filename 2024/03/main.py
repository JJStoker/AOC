import os
import re

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input(sample_filename=None):
    inputs = []

    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        inputs = map(
            lambda l: l.replace("\n", ""), i.readlines()
        )
    return list(inputs)

def part_01():
    instructions = get_input()
    total = sum([
        int(a) * int(b)
        for instruction in instructions
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", instruction)
    ])
    print(f"Day 03, part 1: {total}")

def part_02():
    instructions = "".join(get_input("sample_2"))
    
    mul_regex = r"mul\((\d+),(\d+)\)"
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"

    total = 0
    enabled = True
    for i in re.split(f"({do_regex}|{dont_regex}|{mul_regex})", instructions):
        if not i:
            continue
        if re.fullmatch(do_regex, i):
            enabled = True
        elif re.fullmatch(dont_regex, i):
            enabled = False
        elif enabled and (match := re.match(mul_regex, i)):
            a, b = map(int, match.groups())
            total += a * b

    print(f"Day 03, part 2: {total}")

part_01()
part_02()
