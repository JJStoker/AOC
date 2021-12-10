INPUT_FILE = './sample.txt' if False else './input.txt'

open_chars  = ['{', '[', '<', '(']
close_chars = ['}', ']', '>', ')']

with open(INPUT_FILE, 'r') as input_file:
    navigation_log = list(map(lambda x: x.replace('\n', ''), input_file.readlines()))
    
def part_1():
    score = 0
    score_map  = {')': 3, ']': 57, '}': 1197, '>': 25137}
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

def part_2():
    scores = []
    score_map  = {')': 1, ']': 2, '}': 3, '>': 4}
    for nav_log in navigation_log:
        score = 0
        invalid = False
        unclosed = []
        for c in list(nav_log):
            if invalid: continue
            if c in open_chars:
                unclosed.append(c)
            elif c in close_chars:
                if unclosed[-1] != open_chars[(close_chars.index(c))]:
                    invalid = True
                else:
                    unclosed.pop()
        if not invalid and len(unclosed):
            for x in map(lambda x: close_chars[open_chars.index(x)], reversed(unclosed)):
                score *= 5
                score += score_map[x]
            scores.append(score)
    print (f'Part 2: {sorted(scores)[round(len(scores) // 2)]}')

part_1()
part_2()