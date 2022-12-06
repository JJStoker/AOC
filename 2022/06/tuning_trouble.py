with open('input_01.txt' if True else 'sample.txt', 'r') as i:
    datastream = list(map(lambda l: l.replace("\n", ""), i.readlines()))[0]

def part_01():
    x = 4
    for i in range(x, len(datastream)):
        if len(set(datastream[i-x:i])) == x:
            break
    print (i)

part_01()
