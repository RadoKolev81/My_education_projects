budget = int(input())
season = input()
num_of_fisherman = int(input())
price_for_ship = 0
if season == 'Spring':
    price_for_ship = 3000
    if num_of_fisherman <= 6:
        price_for_ship *= 0.90
    elif 6 < num_of_fisherman <= 11:
        price_for_ship *= 0.85
    elif num_of_fisherman > 11:
        price_for_ship *= 0.75
elif season == 'Summer' or season == 'Autumn':
    price_for_ship = 4200
    if num_of_fisherman <= 6:
        price_for_ship *= 0.90
    elif 6 < num_of_fisherman <= 11:
        price_for_ship *= 0.85
    elif num_of_fisherman > 11:
        price_for_ship *= 0.75
elif season == 'Winter':
    price_for_ship = 2600
    if num_of_fisherman <= 6:
        price_for_ship *= 0.90
    elif 6 < num_of_fisherman <= 11:
        price_for_ship *= 0.85
    elif num_of_fisherman > 11:
        price_for_ship *= 0.75

if num_of_fisherman % 2 == 0 and season != 'Autumn':
    price_for_ship *= 0.95

diff = abs(budget - price_for_ship)
if budget < price_for_ship:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")