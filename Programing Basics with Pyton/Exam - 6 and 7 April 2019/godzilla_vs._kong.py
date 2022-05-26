budget = float(input())
number_of_statists = int(input())
price_for_one_dress = float(input())
price_for_decor = budget * 0.10
price_for_all_dress = price_for_one_dress * number_of_statists

if number_of_statists > 150:
    price_for_all_dress *= 0.90

costs = price_for_decor + price_for_all_dress
diff = abs(budget - costs)

if budget < costs:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")