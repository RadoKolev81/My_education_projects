age = int(input())
price_for_washmachine = float(input())
price_for_toy = int(input())
total_sum = 0
total_toy = 0
brother_money = 0

for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        total_sum += 10 * (current_age / 2)
        brother_money += 1
    else:
        total_toy += 1

saved_money = total_sum + (total_toy * price_for_toy) - brother_money
diff = abs(saved_money - price_for_washmachine)

if saved_money < price_for_washmachine:
    print(f"No! {diff:.2f}")
else:
    print(f"Yes! {diff:.2f}")
