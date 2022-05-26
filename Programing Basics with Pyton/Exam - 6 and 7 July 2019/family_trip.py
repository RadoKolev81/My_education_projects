budget = float(input())
number_of_nights = int(input())
price_for_nights = float(input())
percent_extra_costs = int(input())

if number_of_nights > 7:
    price_for_nights *= 0.95

total_price = number_of_nights * price_for_nights
extra_costs = budget * (percent_extra_costs / 100)
diff = abs(budget - (total_price + extra_costs))

if budget < (total_price + extra_costs):
    print(f"{diff:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")