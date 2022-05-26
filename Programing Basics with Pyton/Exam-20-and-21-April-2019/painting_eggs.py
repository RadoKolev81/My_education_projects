size_of_eggs = input()
color_of_eggs = input()
number_of_batches = int(input())
price_of_eggs = 0

if size_of_eggs == "Large":
    if color_of_eggs == "Red":
        price_of_eggs = 16
    elif color_of_eggs == "Green":
        price_of_eggs = 12
    elif color_of_eggs == "Yellow":
        price_of_eggs = 9
elif size_of_eggs == "Medium":
    if color_of_eggs == "Red":
        price_of_eggs = 13
    elif color_of_eggs == "Green":
        price_of_eggs = 9
    elif color_of_eggs == "Yellow":
        price_of_eggs = 7
elif size_of_eggs == "Small":
    if color_of_eggs == "Red":
        price_of_eggs = 9
    elif color_of_eggs == "Green":
        price_of_eggs = 8
    elif color_of_eggs == "Yellow":
        price_of_eggs = 5

total_price = number_of_batches * price_of_eggs
costs = total_price * 0.35
final_price = total_price - costs
print(f"{final_price:.2f} leva.")
