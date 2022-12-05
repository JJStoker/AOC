from collections import defaultdict

INPUT_FILE = "./sample.txt" if False else "./input.txt"

caves = defaultdict(list)
with open(INPUT_FILE, "r") as input_file:
    for row in map(str.strip, input_file.readlines()):
        (start, end) = row.split('-')
        caves[start].append(end)
        caves[end].append(start)


def cave_explorer(backwards = False):
    paths = 0
    current, traversed, previous = ('start', set(['start']), None)
    traverse = [(current, traversed, previous)]
    # https://en.wikipedia.org/wiki/Depth-first_search
    while traverse:
        (current, traversed, previous) = traverse.pop(0)
        if current == 'end':
            paths += 1
            continue
        for next in caves[current]:
            if next == 'start': continue
            if next not in traversed:
                candidates = set(traversed)
                if next.lower() == next:
                    candidates.add(next)
                traverse.append((next, candidates, previous))
            elif next in traversed and not previous and next != 'end' and backwards:
                traverse.append((next, traversed, next))
    return paths

print(f'Part 1: {cave_explorer(backwards=False)}')
print(f'Part 2: {cave_explorer(backwards=True)}')
