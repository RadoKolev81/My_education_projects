from math import floor

number_of_tournaments = int(input())
start_points = int(input())
total_points = start_points
number_of_wins = 0

for i in range(number_of_tournaments):
    current_stage = input()
    if current_stage == "W":
        total_points += 2000
        number_of_wins += 1
    elif current_stage == "F":
        total_points += 1200
    elif current_stage == "SF":
        total_points += 720

print(f"Final points: {total_points}")
print(f"Average points: {floor((total_points - start_points) / number_of_tournaments)}")
print(f"{(number_of_wins / number_of_tournaments * 100):.2f}%")
