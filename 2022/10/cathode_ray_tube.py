import re
from collections import deque

with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

def solve():
    grid = [[" "] * 40 for _ in range(6)]
    
    signal = 0
    cycle = 0
    x = 1
    def render(x, cycle):
        import os
        os.system("clear")
        if x - 1 <= cycle % 40 <= x + 1:
            grid[cycle // 40][cycle % 40] = '#'
        for i in range(6):
            print(
                "".join(
                    [grid[i][y] for y in range(40)],
                ),
                end="\n",
            )
    
    def update_signal(x, cycle):
        if cycle in [20, 60, 100, 140, 180, 220]:
            return (cycle * x)
        return 0

    for instruction in inputs:
        render(x, cycle)
        cycle += 1
        signal += update_signal(x, cycle)
        cmd = instruction.split()
        if cmd[0] == "addx":
            render(x, cycle)
            cycle += 1
            signal += update_signal(x, cycle)
            x += int(cmd[1])
    
    print(f"Part 1: {signal}")

solve()
