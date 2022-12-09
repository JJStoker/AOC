points = dict(X=1, Y=2, Z=3, A=1, B=2, C=3)

def get_rounds():
    with open('input_01.txt', 'r') as i:
        rounds = map(lambda l: l.replace("\n", ""), i.readlines())
    return rounds

def part_01():
    win = dict(X='C', Y='A', Z='B')
    tie = dict(X='A', Y='B', Z='C')
    lose = dict(X='B', Y='C', Z='A')
    score = 0
    for opponent, my_move in map(lambda x: x.split(" "), get_rounds()):
        score += points[my_move]
        if win[my_move] == opponent:
            score += 6
        elif opponent == tie[my_move]:
            score += 3
    print(score)

def part_02():
    win = dict(A='Y', B='Z', C='X')
    tie = dict(A='X', B='Y', C='Z')
    lose = dict(A='Z', B='X', C='Y')
    
    score = 0
    for opponent, my_move in map(lambda x: x.split(" "), get_rounds()):
        if my_move == "Y":
            score += 3
            score += points[tie[opponent]]
        elif my_move == "X":
            score += points[lose[opponent]]
        elif my_move == "Z":
            score += 6
            score += points[win[opponent]]
    print(score)

part_01()
part_02()
