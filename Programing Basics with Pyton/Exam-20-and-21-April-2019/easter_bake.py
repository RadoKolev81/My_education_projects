from math import ceil

number_of_cakes = int(input())
sugar = 950
flour = 750
max_sugar = 0
max_flour = 0
total_sugar = 0
total_flour = 0

for i in range(number_of_cakes):
    quantity_sugar = int(input())
    quantity_flour = int(input())
    total_sugar += quantity_sugar
    total_flour += quantity_flour

    if quantity_sugar > max_sugar:
        max_sugar = quantity_sugar
    if quantity_flour > max_flour:
        max_flour = quantity_flour

paks_sugar = ceil(total_sugar / sugar)
paks_flour = ceil(total_flour / flour)

print(f"Sugar: {paks_sugar}")
print(f"Flour: {paks_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")