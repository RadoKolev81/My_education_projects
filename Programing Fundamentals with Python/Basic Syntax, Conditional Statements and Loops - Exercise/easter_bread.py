budget = float(input())
price_for_1kg_floor = float(input())
price_for_1pack_eggs = price_for_1kg_floor * 0.75
price_for_250ml_milk = (price_for_1kg_floor * 1.25) / 4
price_for_bread = price_for_1kg_floor + price_for_1pack_eggs + price_for_250ml_milk
number_of_loaves = 0
colored_eggs = 0
money_left = budget

while money_left > price_for_bread:
    money_left -= price_for_bread
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")