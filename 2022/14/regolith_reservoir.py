from collections import defaultdict, deque


with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda p: p.replace('\n', '').split(' -> '), i.readlines()))

def get_grid():
    grid = defaultdict(str)
    # iterate over each path row
    # follow the path, adding a # to each coordinate on the path
    for path in inputs:
        coords = map(lambda coord: tuple(map(int, coord.split(','))), path)
        edges = deque(coords)
        current = edges.pop()
        grid[current] = "#"
        while edges:
            next = edges.pop()
            grid[next] = "#"
            for i in range(min(current[0], next[0]), max(current[0], next[0]) + 1):
                for j in range(min(current[1], next[1]), max(current[1], next[1]) + 1):
                    grid[(i, j)] = '#'
            current = next
        
    return grid

def get_grid_extend(grid):
    min_x, max_x = min(g[0] for g in grid.keys()), max(g[0] for g in grid.keys()) + 1
    min_y, max_y = min(g[1] for g in grid.keys()), max(g[1] for g in grid.keys()) + 1
    return min_x, max_x, min_y, max_y

def dump_grid(grid):
    import os
    os.system("clear")
    min_x, max_x, _, max_y = get_grid_extend(grid)
    for y in range(max_y - 40, max_y):
        print (
            "".join([
                grid[(x, y)] or "." 
                for x in range(min_x, max_x)
            ]),
            end="\n"
        )
    
def part_01():
    current = (500, 0)
    grid = get_grid()
    _, _, _, max_y = get_grid_extend(grid)
    endpoint_y = max_y + 1
    # next nodes are only: down (x + 0, y+1), left + down (x - 1, y + 1) and right + down (x + 1, y + 1)
    get_next_nodes = lambda x, y: [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
    step = 0
    while True:
        next = [n for n in get_next_nodes(*current) if not grid[n]]
        if len(next):
            next = next[0]
        else:
            next = current
        if next == current:
            grid[next] = 'o'
            current = (500, 0)
            if next == (500, 0):
                break
        else:
            if next[1] > endpoint_y:
                break
            current = next
        if step % 240 == 0: dump_grid(grid)
        step += 1
    print(f"Part 1: {len(list(filter(lambda x: x == 'o', grid.values())))}")

part_01()
