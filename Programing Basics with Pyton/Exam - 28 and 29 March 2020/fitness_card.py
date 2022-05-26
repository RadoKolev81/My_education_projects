cash = int(input())
sex = input()
age = int(input())
sport = input()

total_price = 0

if sex == "m":
    if sport == "Gym":
        total_price = 42
    elif sport == "Boxing":
        total_price = 41
    elif sport == "Yoga":
        total_price = 45
    elif sport == "Zumba":
        total_price = 34
    elif sport == "Dances":
        total_price = 51
    elif sport == "Pilates":
        total_price = 39
elif sex == "f":
    if sport == "Gym":
        total_price = 35
    elif sport == "Boxing":
        total_price = 37
    elif sport == "Yoga":
        total_price = 42
    elif sport == "Zumba":
        total_price = 31
    elif sport == "Dances":
        total_price = 53
    elif sport == "Pilates":
        total_price = 37

if age <= 19:
    total_price *= 0.80

if cash >= total_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(cash - total_price)
    print(f"You don't have enough money! You need ${diff:.2f} more.")