def find_start(x):
    with open('input_01.txt' if True else 'sample.txt', 'r') as i:
        datastream = list(map(lambda l: l.replace("\n", ""), i.readlines()))[0]

    for i in range(x, len(datastream)):
        if len(set(datastream[i-x:i])) == x:
            break
    return i

def part_01():
    print (find_start(4))
    
def part_02():
    print (find_start(14))

part_01()
part_02()
