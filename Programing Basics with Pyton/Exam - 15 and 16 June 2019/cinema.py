hall_capacity = int(input())

money_income = 0
hall_is_full = False

while True:
    command = input()
    if command == "Movie time!":
        print(f"There are {hall_capacity} seats left in the cinema.")
        break
    if int(command) > hall_capacity:
        hall_is_full = True
        print("The cinema is full.")
        break
    hall_capacity -= int(command)
    money_income += int(command) * 5
    if int(command) % 3 == 0:
        money_income -= 5

print(f"Cinema income - {money_income} lv.")