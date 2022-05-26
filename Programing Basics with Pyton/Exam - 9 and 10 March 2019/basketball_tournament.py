all_games = 0
wins = 0
losts = 0
name_of_tournament = input()
while name_of_tournament != 'End of tournaments':
    number_of_games = int(input())
    all_games += number_of_games
    game_number = 0
    for i in range(1, number_of_games + 1):
        points_1_team = int(input())
        points_2_team = int(input())
        if points_1_team > points_2_team:
            game_number += 1
            wins += 1
            print(f"Game {game_number} of tournament {name_of_tournament}: "
                  f"win with {points_1_team - points_2_team} points.")
        elif points_2_team > points_1_team:
            game_number += 1
            losts += 1
            print(f"Game {game_number} of tournament {name_of_tournament}: "
                  f"lost with {points_2_team - points_1_team} points.")

    name_of_tournament = input()

print(f"{(wins / all_games * 100):.2f}% matches win")
print(f"{(losts / all_games * 100):.2f}% matches lost")
