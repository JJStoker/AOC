INPUT_FILE = "./sample.txt" if False else "./input.txt"

max_y, min_y, max_x, min_x = 0, 0, 0, 0
with open(INPUT_FILE, "r") as input_file:
    x, y = input_file.read().strip().replace(' ', '').split(':')[1].split(',')
    xs = list(map(int, x.strip('x=').split('..')))
    ys = list(map(int, y.strip('y=').split('..')))
    max_x, min_x = max(xs), min(xs)
    max_y, min_y = max(ys), min(ys)

def part_1():
    print(f'Part 1: {(min_y * (min_y + 1)) // 2}')
    
part_1()
