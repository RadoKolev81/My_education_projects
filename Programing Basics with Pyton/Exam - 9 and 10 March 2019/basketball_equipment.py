year_tax = int(input())

price_for_sneakers = year_tax * 0.60
price_for_equip = price_for_sneakers * 0.80
price_for_ball = price_for_equip / 4
price_for_accessory = price_for_ball / 5
total_costs = year_tax + price_for_sneakers + price_for_equip + price_for_ball + price_for_accessory
print(f"{total_costs:.2f}")
