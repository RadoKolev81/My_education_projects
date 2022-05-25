budget = float(input())
num_of_stats = int(input())
price_one_dress = float(input())
deckor = budget * 0.10
price_for_all_dress = num_of_stats * price_one_dress

if num_of_stats > 150:
    price_for_all_dress *= 0.90

total_cost = deckor + price_for_all_dress
diff = abs(budget - total_cost)
if budget < total_cost:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
