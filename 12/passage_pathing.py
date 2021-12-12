from collections import defaultdict

INPUT_FILE = "./sample.txt" if False else "./input.txt"

caves = defaultdict(list)
with open(INPUT_FILE, "r") as input_file:
    for row in map(str.strip, input_file.readlines()):
        (start, end) = row.split('-')
        caves[start].append(end)
        caves[end].append(start)


def part_1():
    paths = 0
    traverse = []
    traverse.append(('start', set(['start'])))
    while traverse:
        (curr, seen) = traverse.pop(0)
        if curr == 'end':
            paths += 1
            continue
        for next in caves[curr]:
            if next not in seen:
                candidates = set(seen)
                if next.lower() == next:
                    candidates.add(next)
                traverse.append((next, candidates))
    print(f'Part 1: {paths}')

part_1()
