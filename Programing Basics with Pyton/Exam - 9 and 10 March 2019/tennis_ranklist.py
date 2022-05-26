from math import floor

numb_of_tournaments = int(input())
start_points = int(input())
total_points = 0
wins = 0

for i in range(numb_of_tournaments):
    stage_of_tournament = input()

    if stage_of_tournament == 'W':
        total_points += 2000
        wins += 1
    elif stage_of_tournament == 'F':
        total_points += 1200
    elif stage_of_tournament == 'SF':
        total_points += 720

print(f"Final points: {total_points + start_points}")
print(f"Average points: {floor(total_points / numb_of_tournaments)}")
print(f"{(wins / numb_of_tournaments * 100):.2f}%")