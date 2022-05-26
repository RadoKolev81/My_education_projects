price_for_strawberry = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberry = float(input())
kg_strawberry = float(input())

price_for_raspberry = price_for_strawberry / 2
price_for_oranges = price_for_raspberry - (price_for_raspberry * 0.40)
price_for_bananas = price_for_raspberry - (price_for_raspberry * 0.80)

total_price = (kg_bananas * price_for_bananas) + (kg_oranges * price_for_oranges) + \
              (kg_raspberry * price_for_raspberry) + (kg_strawberry * price_for_strawberry)

print(f"{total_price:.2f}")
