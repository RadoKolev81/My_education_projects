type_of_fuel = input()
lt_fuel = float(input())
club_card = input()
price_of_fuel = 0

if type_of_fuel == "Gasoline":
    price_of_fuel = 2.22
    if club_card == "Yes":
        price_of_fuel -= 0.18
    if 20 <= lt_fuel <= 25:
        price_of_fuel *= 0.92
    elif lt_fuel > 25:
        price_of_fuel *= 0.90
elif type_of_fuel == "Diesel":
    price_of_fuel = 2.33
    if club_card == "Yes":
        price_of_fuel -= 0.12
    if 20 <= lt_fuel <= 25:
        price_of_fuel *= 0.92
    elif lt_fuel > 25:
        price_of_fuel *= 0.90
else:
    price_of_fuel = 0.93
    if club_card == "Yes":
        price_of_fuel -= 0.08
    if 20 <= lt_fuel <= 25:
        price_of_fuel *= 0.92
    elif lt_fuel > 25:
        price_of_fuel *= 0.90

total_price = lt_fuel * price_of_fuel
print(f"{total_price:.2f} lv.")