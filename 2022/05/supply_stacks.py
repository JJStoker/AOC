import re

from collections import deque


def get_initial_state():
    with open("input_01.txt", "r") as i:
        inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))
        stacks = {
            1: deque(["F", "L", "M", "W"]),
            2: deque(["F", "M", "V", "Z", "B"]),
            3: deque(["Q", "L", "S", "R", "V", "H"]),
            4: deque(["J", "T", "M", "P", "Q", "V", "S", "F"]),
            5: deque(["W", "S", "L"]),
            6: deque(["W", "J", "R", "M", "P", "V", "F"]),
            7: deque(["F", "R", "N", "P", "C", "Q", "J"]),
            8: deque(["B", "R", "W", "Z", "S", "P", "H", "V"]),
            9: deque(["W", "Z", "H", "G", "C", "J", "M", "B"]),
        }
        instructions = inputs[10:]
    return stacks, instructions


def part_01():
    stacks, instructions = get_initial_state()
    for instruction in instructions:
        n, start, end = map(int, re.search(r'move (\d+) from (\d+) to (\d+)', instruction).groups())
        for _ in range(n):
            d = stacks[start].popleft()
            if d:
                stacks[end].appendleft(d)
    print("".join([stack.popleft() for stack in stacks.values()]))
    
def part_02():
    stacks, instructions = get_initial_state()
    for instruction in instructions:
        n, start, end = map(int, re.search(r'move (\d+) from (\d+) to (\d+)', instruction).groups())
        crates = []
        for _ in range(n):
            crates.append(stacks[start].popleft())
        for crate in reversed(crates):
            stacks[end].appendleft(crate)
    print("".join([stack.popleft() for stack in stacks.values()]))
    
part_01()
part_02()
