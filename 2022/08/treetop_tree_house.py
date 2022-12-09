from functools import reduce

with open('input.txt' if True else 'sample.txt', 'r') as i:
    rows = list(map(lambda l: l.replace("\n", ""), i.readlines()))

def is_edge(x, y):
    return x == 0 or y == 0 or x == len(rows[0]) -1 or y == len(rows) -1

def is_visible(x, y):
    up = all((rows[x][y] > t for t in rows[x][:y]))
    down = all((rows[x][y] > t for t in rows[x][y + 1:]))
    left = all(rows[x][y] > rows[i][y] for i in range(x - 1, -1, -1))
    right = all(rows[x][y] > rows[i][y] for i in range(x + 1, len(rows)))
    return up or down or left or right

def scenic_score(x, y):
    if is_edge(x, y): return 0
    up, down, left, right = 0, 0, 0, 0
    for t in reversed(rows[x][:y]):
        if rows[x][y] > t:
            up += 1
        else:
            up += 1
            break
    for t in rows[x][y + 1:]:
        if rows[x][y] > t:
            down += 1
        else:
            down += 1
            break
    for i in range(x - 1, -1, -1):
        if rows[x][y] > rows[i][y]:
            left += 1
        else:
            left += 1
            break
    for i in range(x + 1, len(rows)):
        if rows[x][y] > rows[i][y]:
            right += 1
        else:
            right += 1
            break
    return reduce(lambda a, b: a * b, [up, down, left, right])

def get_visible_trees():
    visible = []
    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):
            if is_edge(rx, cx) or is_visible(rx, cx):
                visible.append((rx, cx))
    return visible

def part_01():
    print(f"Part 1: {len(get_visible_trees())}")

def part_02():
    print (f"Part 2: {max(map(lambda tree: scenic_score(tree[0], tree[1]), get_visible_trees()))}")

part_01()
part_02()
