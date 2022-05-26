fruit = input()
size = input()
number_of_order = int(input())

total_price = 0

if size == "small":
    if fruit == "Watermelon":
        total_price += 2 * 56
    elif fruit == "Mango":
        total_price += 2 * 36.66
    elif fruit == "Pineapple":
        total_price += 2 * 42.10
    elif fruit == "Raspberry":
        total_price += 2 * 20
elif size == "big":
    if fruit == "Watermelon":
        total_price += 5 * 28.70
    elif fruit == "Mango":
        total_price += 5 * 19.60
    elif fruit == "Pineapple":
        total_price += 5 * 24.80
    elif fruit == "Raspberry":
        total_price += 5 * 15.20

final_price = total_price * number_of_order

if 400 <= final_price <= 1000:
    final_price *= 0.85
elif final_price > 1000:
    final_price *= 0.50

print(f"{final_price:.2f} lv.")