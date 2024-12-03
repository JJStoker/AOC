import os
import re

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input():
    inputs = []

    with open("sample.txt" if DEBUG else "input.txt", "r") as i:
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
    pass

part_01()
part_02()
