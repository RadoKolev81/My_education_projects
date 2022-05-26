p1_name = input()
p2_name = input()
p1_points = 0
p2_points = 0
is_number_wars = False

while True:
    p1_kard = input()
    if p1_kard == 'End of game':
        break
    p2_kard = input()
    p1_kard = int(p1_kard)
    p2_kard = int(p2_kard)
    if p1_kard > p2_kard:
        p1_points += (p1_kard - p2_kard)
    elif p1_kard < p2_kard:
        p2_points += (p2_kard - p1_kard)
    else:
        another_p1_kard = int(input())
        another_p2_kard = int(input())
        is_number_wars = True
        print("Number wars!")
        if another_p1_kard > another_p2_kard:
            p1_points += (p1_kard - p2_kard)
            print(f"{p1_name} is winner with {p1_points} points")
            break
        elif another_p1_kard < another_p2_kard:
            p2_points += (p2_kard - p1_kard)
            print(f"{p2_name} is winner with {p2_points} points")
            break
if not is_number_wars:
    print(f"{p1_name} has {p1_points} points")
    print(f"{p2_name} has {p2_points} points")
