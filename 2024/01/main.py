import os

DEBUG = os.getenv('DEBUG', 'off').lower() == 'on'


def get_input():
    items = []

    with open('sample.txt' if DEBUG else 'input.txt', 'r') as i:
        items = map(
            lambda l: map(int, l.replace("\n", "").split('   ')),
            i.readlines()
        )
    return list(items)

def part_01():
    a, b = list(zip(*get_input()))
    distances = []
    for x, y in zip(sorted(a), sorted(b)):
        distances.append(abs(x - y))
    print (F'Day 01, part 1: {sum(distances)}')

def part_02():
    a, b = list(zip(*get_input()))
    similarity_score = []
    
    def similarity(n):
        return n * len([i for i in b if i == n])
    
    for x in a:
        similarity_score.append(similarity(x))
    print (F'Day 01, part 2: {sum(similarity_score)}')

part_01()
part_02()