days = int(input())
food = float(input())
biscuits = 0
total_food = 0
dog = 0
cat = 0
for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    dog += dog_food
    cat += cat_food
    total_food += dog_food + cat_food
    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(total_food / food * 100):.2f}% of the food has been eaten.")
print(f"{(dog / total_food * 100):.2f}% eaten from the dog.")
print(f"{(cat / total_food * 100):.2f}% eaten from the cat.")
