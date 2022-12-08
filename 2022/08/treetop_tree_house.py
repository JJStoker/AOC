with open('input.txt' if False else 'sample.txt', 'r') as i:
    rows = list(map(lambda l: l.replace("\n", ""), i.readlines()))

def is_edge(x, y):
    return x == 0 or y == 0 or x == len(rows[0]) -1 or y == len(rows) -1

def is_visible(x, y):
    up = all((rows[x][y] > t for t in rows[x][:y]))
    down = all((rows[x][y] > t for t in rows[x][y + 1:]))
    left = all(rows[x][y] > rows[i][y] for i in range(x - 1, -1, -1))
    right = all(rows[x][y] > rows[i][y] for i in range(x + 1, len(rows)))
    return up or down or left or right

def part_01():
    visible = []
    for rx, row in enumerate(rows):
        for cx, col in enumerate(row):
            if is_edge(rx, cx) or is_visible(rx, cx):
                visible.append((rx, cx))
    print(f"Part 1: {len(visible)}")

part_01()
