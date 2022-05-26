number_of_guests = int(input())
price_for_one = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    price_for_one *= 0.85
elif 15 < number_of_guests <= 20:
    price_for_one *= 0.80
elif number_of_guests > 20:
    price_for_one *= 0.75

price_for_cake = budget * 0.10
total_costs = number_of_guests * price_for_one + price_for_cake
diff = abs(budget - total_costs)

if budget < total_costs:
    print(f"No party! {diff:.2f} leva needed.")
else:
    print(f"It is party time! {diff:.2f} leva left.")