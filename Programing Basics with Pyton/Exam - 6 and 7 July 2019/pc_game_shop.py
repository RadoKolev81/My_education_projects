numb_of_sell_game = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(numb_of_sell_game):
    name_of_game = input()

    if name_of_game == "Hearthstone":
        hearthstone += 1
    elif name_of_game == "Fornite":
        fornite += 1
    elif name_of_game == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {(hearthstone / numb_of_sell_game * 100):.2f}%")
print(f"Fornite - {(fornite / numb_of_sell_game * 100):.2f}%")
print(f"Overwatch - {(overwatch / numb_of_sell_game * 100):.2f}%")
print(f"Others - {(others / numb_of_sell_game * 100):.2f}%")
