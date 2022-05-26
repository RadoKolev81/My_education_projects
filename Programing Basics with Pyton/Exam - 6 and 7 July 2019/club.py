target_profit = float(input())

total_price = 0

while True:
    cocktail = input()
    if cocktail == "Party!":
        break
    num_cocktails = int(input())

    price = len(cocktail)
    cocktails_price = price * num_cocktails

    if cocktails_price % 2 != 0:
        cocktails_price *= 0.75

    total_price += cocktails_price

    if total_price >= target_profit:
        break

if total_price >= target_profit:
    print("Target acquired.")
else:
    difference = abs(target_profit - total_price)
    print(f"We need {difference:.2f} leva more.")

print(f"Club income - {total_price:.2f} leva.")