from collections import defaultdict

INPUT_FILE = './sample.txt' if False else './input.txt'

linesegments = []
with open(INPUT_FILE, 'r') as input_file:
    for [coord1, _, coord2] in filter(lambda x: x != '->', map(str.split, map(str.strip, input_file.readlines()))):
        linesegments.append([list(map(int, coord1.split(','))), list(map(int, coord2.split(',')))])

def part_1():
    grid = defaultdict(int)
    for [[x1, y1], [x2, y2]] in linesegments:
        if (x1 != x2 and y1 != y2): continue
        rx, rxx = min(x1, x2), max(x1, x2)
        ry, ryy = min(y1, y2), max(y1, y2)
        for x in range(rx, rxx + 1):
            for y in range(ry, ryy + 1):
                grid[(x, y)] += 1
    print(f'Part 1: {len(list(filter(lambda x: x > 1, grid.values())))}')

part_1()
