player_name = input()
start_points = 301
shot_counter = 0
bad_shot_counter = 0

while True:
    area = input()
    if area == 'Retire':
        print(f"{player_name} retired after {bad_shot_counter} unsuccessful shots.")
        break
    points = int(input())
    shot_counter += 1
    if area == 'Single':
        start_points -= points
        current_points = points
        if start_points < 0:
            shot_counter -= 1
            bad_shot_counter += 1
            start_points += current_points
    elif area == 'Double':
        start_points -= (points * 2)
        current_points = (points * 2)
        if start_points < 0:
            shot_counter -= 1
            bad_shot_counter += 1
            start_points += current_points
    elif area == 'Triple':
        start_points -= (points * 3)
        current_points = (points * 3)
        if start_points < 0:
            shot_counter -= 1
            bad_shot_counter += 1
            start_points += current_points

    if start_points == 0:
        print(f"{player_name} won the leg with {shot_counter} shots.")
        break
