from typing import List, Tuple

INPUT_FILE = './sample.txt' if False else './input.txt'

with open(INPUT_FILE, 'r') as input_file:
    navigation_log = list(map(lambda x: x.replace('\n', ''), input_file.readlines()))
    
def part_1():
    score = 0
    score_map  = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_chars  = ['{', '[', '<', '(']
    close_chars = ['}', ']', '>', ')']
    for nav_log in navigation_log:
        unclosed = []
        for (i, c) in enumerate(list(nav_log)):
            if c in open_chars:
                unclosed.append(c)
            elif c in close_chars:
                if unclosed[-1] != open_chars[(close_chars.index(c))]:
                    score += score_map[c]
                    break;
                else:
                    unclosed.pop()
    print(f'Part 1: {score}')

part_1()