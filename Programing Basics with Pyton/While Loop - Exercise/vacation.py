needed_money = float(input())
money = float(input())

spend_days = 0
days_counter = 0

while True:
    command = input()
    current_money = float(input())
    days_counter += 1
    if command == "spend":
        money -= current_money
        spend_days += 1
        if money < 0:
            money = 0
    if spend_days > 4:
        print(f"You can't save the money.")
        print(f"{days_counter}")
        break
    elif command == "save":
        money += current_money
        spend_days = 0
        if money >= needed_money:
            print(f"You saved the money for {days_counter} days.")
            break