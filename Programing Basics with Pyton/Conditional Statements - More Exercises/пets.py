from math import ceil, floor

count_of_days = int(input())
kg_leaved_food = int(input())
kg_dog_food_for_day = float(input())
kg_cat_food_for_day = float(input())
gr_turtle_food_for_day = float(input())
kg_turtle_food_for_day = gr_turtle_food_for_day / 1000
total_food = (kg_turtle_food_for_day * count_of_days) + (kg_cat_food_for_day * count_of_days) + \
             (kg_dog_food_for_day * count_of_days)
diff = abs(kg_leaved_food - total_food)
if total_food > kg_leaved_food:
    print(f'{ceil(diff)} more kilos of food are needed.')
else:
    print(f'{floor(diff)} kilos of food left.')
