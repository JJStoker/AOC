

def part_01(sample=False):
    with open('sample.txt' if sample else 'input.txt', 'r') as i:
        items = map(
            lambda l: map(int, l.replace("\n", "").split('   ')),
            i.readlines()
        )
    
    a, b = list(zip(*items))
    distances = []
    for x, y in zip(sorted(a), sorted(b)):
        distances.append(abs(x - y))
    print (sum(distances))

part_01()