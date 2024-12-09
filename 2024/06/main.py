import os
import time

DEBUG = os.getenv("DEBUG", "off").lower() == "on"

# directions to move in the grid
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

# new heading after a right turn
right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
# signs to fill in whenever we traversed a path
headed_sign = {'^': '|', '>': '-', 'v': '|', '<': '-'}
# unique path signs
path_signs = { '-', '|', 'x', 'O', '+', "^" }

corner_sign = '+'



def clear_terminal():
    """Clears the terminal screen."""
    print("\033[2J\033[H", end="")

def print_grid(grid, delay=0.1, highlight=None):
    """
    Prints the grid to the terminal with smooth updates.
    
    Parameters:
    - grid: 2D list representing the grid.
    - delay: Time delay between updates (in seconds).
    - highlight: Optional tuple (y, x) to highlight a specific cell.
    """
    clear_terminal()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if highlight == (y, x):
                # Highlight cell with inverted colors
                print(f"\033[7m{cell}\033[0m", end="")
            else:
                print(cell, end="")
        print()  # Move to the next row
    time.sleep(delay)

def get_input(sample_filename=None):
    input = []
    initial_position = (0, 0)
    with open(f"{sample_filename or "sample"}.txt" if DEBUG else "input.txt", "r") as i:
        for line in i.readlines():
            if line == "\n":
                continue
            row = list(line.strip())
            for d in directions.keys():
                if d in row:
                    initial_position = (len(input), row.index(d), )
            input.append(row)
    return input, initial_position

def part_01():
    grid, initial_position = get_input()
    traversed = { initial_position }
    heading = grid[initial_position[0]][initial_position[1]]
    y, x = initial_position
    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        dy, dx = directions[heading]
        ny, nx = y + dy, x + dx
        if (
            ny >= len(grid)
            or nx >= len(grid[0])
            or ny < 0
            or nx < 0
        ):
            break
        if grid[ny][nx] == '#':
            heading = right_turn[heading]
        else:
            traversed.add((ny, nx))
            x, y = nx, ny
    print(f"Day 06, part 1: {len(traversed)}")

def part_02():
    grid, initial_position = get_input()
    y, x = initial_position
    
    positions = 0
    loops = []
    
    obstacles = { (y, x) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '#' }
    
    print (obstacles)
    
    def loops_around(y, x, grid):
        heading = grid[y][x]
        traversed = { (y, x, heading) }
        while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            # print_grid(grid, delay=0.0001, highlight=(y, x))
            dy, dx = directions[heading]
            ny, nx = y + dy, x + dx
            if (
                ny >= len(grid)
                or nx >= len(grid[0])
                or ny < 0
                or nx < 0
            ):
                return False
            if grid[ny][nx] == '#' or grid[ny][nx] == 'O':
                heading = right_turn[heading]
                grid[y][x] = corner_sign
                continue
            if (ny, nx, heading) in traversed:
                return True
            traversed.add((ny, nx, heading))
            grid[ny][nx] = headed_sign[heading]
            x, y = nx, ny
        return False
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in obstacles or (y, x) == initial_position:
                continue
            grid_copy = [col[:] for col in grid]
            grid_copy[y][x] = 'O'
            if loops_around(*initial_position, grid_copy):
                positions += 1
                loops.append(grid_copy)
    print(f"Day 06, part 2: {positions}")
        

part_01()
part_02()
