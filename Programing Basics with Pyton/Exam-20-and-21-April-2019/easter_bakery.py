price_for_flour_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
num_of_eggs = int(input())
maya_packs = int(input())

price_for_sugar = price_for_flour_kg * 0.75
price_for_eggs = price_for_flour_kg * 1.10
price_for_maya_packs = price_for_sugar * 0.20
sum_for_flour = kg_flour * price_for_flour_kg
sum_for_sugar = kg_sugar * price_for_sugar
sum_for_eggs = num_of_eggs * price_for_eggs
sum_for_maya = maya_packs * price_for_maya_packs
total_sum = sum_for_flour + sum_for_sugar + sum_for_eggs + sum_for_maya
print(f"{total_sum:.2f}")
