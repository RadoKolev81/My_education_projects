name_of_team = input()
numb_of_games = int(input())

wins = 0
drafts = 0
losts = 0
total_points = 0
dont_play = False

if numb_of_games == 0:
    dont_play = True

for i in range(numb_of_games):
    result = input()

    if result == "W":
        wins += 1
        total_points += 3
    elif result == "D":
        drafts += 1
        total_points += 1
    elif result == "L":
        losts += 1

if dont_play:
    print(f"{name_of_team} hasn't played any games during this season.")
else:
    print(f"{name_of_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {drafts}")
    print(f"## L: {losts}")
    print(f"Win rate: {(wins / numb_of_games * 100):.2f}%")
