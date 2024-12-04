import os

DEBUG = os.getenv("DEBUG", "off").lower() == "on"


def get_input(sample_filename=None):
    inputs = []

    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        inputs = map(
            lambda l: list(l.replace("\n", "")),
            i.readlines()
        )
    return list(inputs)

def part_01():
    grid = get_input()
    directions = [
        (0, -1),  # up
        (1, -1),  # up-right
        (1, 0),   # right
        (1, 1),   # down-right
        (0, 1),   # down
        (-1, 1),  # down-left
        (-1, 0),  # left
        (-1, -1), # up-left
    ]

    target = ['X', 'M', 'A', 'S']
    
    xmas = []
    
    def find_xmas(start_x, start_y, dx, dy):
        x, y = start_x, start_y
        chars = []
        while True:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
                break
            chars.append(grid[y][x])
            if len(chars) == 4:
                break
            x += dx
            y += dy
        matches_xmas = chars == target
        if matches_xmas:
            xmas.append(chars)
        return matches_xmas
    
    
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '.':
                continue
            for dx, dy in directions:
                find_xmas(x, y, dx, dy)
            
    print(f"Day 04, part 1: {len(xmas)}")

def part_02():
    grid = get_input()
    right_up = (1, -1)
    right_down = (1, 1)
    
    target_mas = ['M', 'A', 'S']
    target_sam = ['S', 'A', 'M']
    
    xmas = 0
    
    def find_xmas(start_x, start_y, dx, dy):
        x, y = start_x, start_y
        chars = []
        while True:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
                break
            chars.append(grid[y][x])
            if len(chars) == 3:
                break
            x += dx
            y += dy
        matches_mas = chars == target_mas
        matches_sam = chars == target_sam
        return matches_mas or matches_sam
    
    
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if (
                y + 1 >= len(grid)
                or x + 1 >= len(grid[y])
                or grid[y + 1][x + 1] != 'A'
            ):
                continue
            if (
                
                find_xmas(x, y, *right_down)
                and find_xmas(x, y + 2, *right_up)
            ):
                xmas += 1
    print(f"Day 04, part 2: {xmas}")

part_01()
part_02()
