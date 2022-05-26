
best_result = 0
best_player = ""
hat_trick = False

while True:
    player_name = input()
    if player_name == "END":
        break

    numb_of_goals = int(input())
    if numb_of_goals > best_result:
        best_result = numb_of_goals
        best_player = player_name
    if numb_of_goals >= 3:
        hat_trick = True
        if numb_of_goals >= 10:
            break

print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {best_result} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_result} goals.")
