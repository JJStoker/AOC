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
        (0, -1), 
        (1, -1), 
        (1, 0),  
        (1, 1),  
        (0, 1),  
        (-1, 1), 
        (-1, 0), 
        (-1, -1),
    ]
    
    target = ['X', 'M', 'A', 'S']
    
    xmas = []
    
    def find_xmas(start_x, start_y, dx, dy):
        x, y = start_x, start_y
        chars = []
        coords = []
        while True:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
                break
            chars.append(grid[y][x])
            coords.append((y, x))
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
    pass
    xmas = []
    print(f"Day 04, part 2: {len(xmas)}")

if __name__ == '__main__':
    part_01()
    part_02()

