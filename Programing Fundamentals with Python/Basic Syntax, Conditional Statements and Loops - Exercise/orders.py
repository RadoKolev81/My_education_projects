number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    amount_of_capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if amount_of_capsules < 1 or amount_of_capsules > 2000:
        continue
    current_price = price_per_capsule * amount_of_capsules * days
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${total_price:.2f}")