from collections import defaultdict

with open("input.txt" if True else "sample.txt", "r") as i:
    rows = list(map(lambda l: l.replace("\n", ""), i.readlines()))

grid = defaultdict(str)

def sign(x):
    return (x > 0) - (x < 0)

def move_tail_element(e1, e2):
    xdelta = e1[0] - e2[0]
    ydelta = e1[1] - e2[1]
    if abs(xdelta) > 1 or abs(ydelta) > 1:
        e2[0] += (xdelta > 0) - (xdelta < 0)
        e2[1] += (ydelta > 0) - (ydelta < 0)

def move_head(h, dir):
    h[0] += 1 if dir == 'R' else -1 if dir == 'L' else 0
    h[1] += 1 if dir == 'D' else -1 if dir == 'U' else 0

def move(rope, direction):
    move_head(rope[0], direction)

    for i in range(1, len(rope)):
        grid[tuple(rope[i])] = "T"
        move_tail_element(rope[i-1], rope[i])
    grid[tuple(rope[i])] = "T"
    grid[tuple(rope[0])] = "H"
    return tuple(rope[-1])

def simulate(rope):
    return set(
        move(rope, direction)
        for direction, n in map(str.split, rows)
        for _ in range(int(n))
    )

def dump_grid():
    for x in range(-100, 100):
        print(
            "".join(
                map(
                    lambda x: f'{"■" if x == "H" else "□" if x == "T" else "."}',
                    [grid[(x, y)] for y in range(-100, 100)],
                )
            ),
            end="\n",
        )

def part_01():
    print(f"Part 1: {len(simulate([[0, 0] for _ in range(2)]))}")

def part_02():
    print(f"Part 2: {len(simulate([[0, 0] for _ in range(10)]))}")

part_01()
part_02()

dump_grid()