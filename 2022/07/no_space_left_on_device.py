import re
from collections import defaultdict

def get_sizes():
    sizes = defaultdict(int)
    sizes["/root"] = 0
    with open('input.txt' if True else 'sample.txt', 'r') as i:
        output = list(map(lambda l: l.replace("\n", ""), i.readlines()))
    curr_folder = "/root"
    for line in output:
        cmd = re.search(r'\$ (cd|ls) (.+)', line)
        if cmd:
            op, folder = cmd.groups()
            if op in ["dir", "ls"]: continue
            if op == "cd":
                if folder == "/":
                    curr_folder = "/root"
                elif folder == "..":
                    curr_folder = curr_folder[0:curr_folder.rfind("/")]
                else:
                    curr_folder += f'/{folder}'

        file_size = re.search(r'(\d+) (.+)', line)
        if file_size:
            size, file = file_size.groups()
            folder = curr_folder
            for _ in range(curr_folder.count("/")):
                sizes[folder] += int(size)
                folder = folder[:folder.rfind("/")]
    return sizes
    
def part_01():
    sizes = get_sizes()
    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size
    print(f"Part 1: {total}")

def part_02():
    sizes = get_sizes()
    target = sizes["/root"] - 39999999
    folders = []
    for size in sizes.values():
        if target <= size:
            folders.append(size)
    print(f"Part 2: {min(folders)}")


part_01()
part_02()