budget = float(input())
num_vgus = int(input())
num_cpus = int(input())
num_rams = int(input())
price_for_vgus = num_vgus * 250
price_for_cpus = num_cpus * price_for_vgus * 0.35
price_for_rams = num_rams * price_for_vgus * 0.10
total_price = price_for_vgus + price_for_cpus + price_for_rams

if num_vgus > num_cpus:
    total_price *= 0.85

diff = abs(budget - total_price)
if budget < total_price:
    print(f'Not enough money! You need {diff:.2f} leva more!')
else:
    print(f'You have {diff:.2f} leva left!')