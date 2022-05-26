budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_extra_cost = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

costs = number_of_nights * price_per_night
additional_cost = budget * (percent_extra_cost / 100)
total_sum = costs + additional_cost
diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")