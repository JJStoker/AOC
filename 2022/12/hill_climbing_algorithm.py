from string import ascii_lowercase as alc, ascii_uppercase as upc
from collections import deque

score_map = {x: c for c, x in enumerate(alc)}
with open("input.txt" if True else "sample.txt", "r") as i:
    inputs = list(map(lambda l: l.replace("\n", ""), i.readlines()))

height = len(inputs)
width = len(inputs[0])
grid = {(x, y): inputs[y][x] for y in range(height) for x in range(width)}
start = [t for t, c in grid.items() if c == "S"][0]
end = [t for t, c in grid.items() if c == "E"][0]
score_grid = {t: score_map[grid[t].lower()] for t in grid.keys()}
score_grid[start] = score_map['a']
score_grid[end] = score_map['z']

def part_01():
    movements = ((0, -1), (0, 1), (-1, 0), (1, 0))
    traveled = 0
    handled = set()
    handled.add(start)
    stack = deque()
    stack.appendleft((0, start))
    # see 2021/09 -> breadth width search
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
    
part_01()
