# Цената на един литър гориво е 2.10 лв.
# Цената за екскурзовод е 100лв.
# В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

budget = float(input())
need_fuel = float(input())
day_of_week = input()

price_for_fuel = need_fuel * 2.10
price_for_git = 100
total_price = price_for_git + price_for_fuel
if day_of_week == "Saturday":
    total_price *= 0.90
elif day_of_week == "Sunday":
    total_price *= 0.80

diff = abs(budget - total_price)
if budget < total_price:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
else:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
