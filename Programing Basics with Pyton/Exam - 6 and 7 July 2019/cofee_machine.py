drink = input()
sugar = input()
number_of_drinks = int(input())
price_for_drink = 0
if drink == "Espresso":
    if sugar == "Without":
        price_for_drink = 0.90
    elif sugar == "Normal":
        price_for_drink = 1
    elif sugar == "Extra":
        price_for_drink = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price_for_drink = 1.00
    elif sugar == "Normal":
        price_for_drink = 1.20
    elif sugar == "Extra":
        price_for_drink = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price_for_drink = 0.50
    elif sugar == "Normal":
        price_for_drink = 0.60
    elif sugar == "Extra":
        price_for_drink = 0.70

if sugar == "Without":
    price_for_drink *= 0.65
if drink == "Espresso" and number_of_drinks >= 5:
    price_for_drink *= 0.75
total_price = number_of_drinks * price_for_drink
if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")