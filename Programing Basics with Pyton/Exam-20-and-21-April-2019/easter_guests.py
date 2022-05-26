from math import ceil

number_of_guests = int(input())
budget = int(input())

number_of_cakes = ceil(number_of_guests / 3)
number_of_eggs = number_of_guests * 2
price_for_cakes = number_of_cakes * 4
price_for_eggs = number_of_eggs * 0.45
total_price = price_for_eggs + price_for_cakes
diff = abs(budget - total_price)
if budget < total_price:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
else:
    print(f"Lyubo bought {number_of_cakes} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
