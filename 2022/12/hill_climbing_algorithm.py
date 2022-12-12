from string import ascii_lowercase as alc, ascii_uppercase as upc
from collections import deque

score_map = {x: c + 1 for c, x in enumerate(alc)}
movements = ((0, -1), (0, 1), (-1, 0), (1, 0))
def get_grid():
    with open("input.txt" if True else "sample.txt", "r") as i:
        inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

    height = len(inputs)
    width = len(inputs[0])
    grid = {(x, y): inputs[y][x] for y in range(height) for x in range(width)}

    score_grid = {
        t: {"S": 1, "E": 27}.get(grid[t], score_map[grid[t].lower()])
        for t in grid.keys()
    }
    return score_grid, grid

def part_01():
    # see 2021/09 -> breadth-first search
    score_grid, grid = get_grid()
    start = [t for t, c in grid.items() if c == "S"][0]
    end = [t for t, c in grid.items() if c == "E"][0]
    traveled = 0
    handled = set([start])
    stack = deque([(0, start)])
    while stack:
        distance, node = stack.popleft()
        if node == end:
            traveled = distance
            break
        node_score = score_grid[node]
        for mov in movements:
            next_pos = (node[0] + mov[0], node[1] + mov[1])
            if next_pos not in score_grid or next_pos in handled:
                continue
            next_score = score_grid[next_pos]
            if node_score + 1 >= next_score:
                next_distance = distance + 1
                handled.add(next_pos)
                stack.append((next_distance, next_pos))
        
    print(f'Part 1: {traveled}')
    
def part_02():
    # the trick is to reverse the search, so find the nearest path to height=1 (a)
    score_grid, grid = get_grid()
    end = [t for t, c in grid.items() if c == "E"][0]
    traveled = 0
    handled = set([end])
    stack = deque([(0, end)])
    while stack:
        distance, node = stack.popleft()
        height = score_grid[node]
        # we traveled from the highest point (end) to a low point
        if height == 1: 
            traveled = distance
            break
        node_score = score_grid[node]
        for mov in movements:
            next_pos = (node[0] + mov[0], node[1] + mov[1])
            if next_pos not in score_grid or next_pos in handled:
                continue
            next_score = score_grid[next_pos]
            if node_score -1 <= next_score:
                next_distance = distance + 1
                handled.add(next_pos)
                stack.append((next_distance, next_pos))
        
    print(f'Part 2: {traveled}')
    
part_01()
part_02()
