from math import floor, ceil

the_vineyard_sq_mt = int(input())
grape_for_sq_mt = float(input())
needed_wine_lt = int(input())
num_workers = int(input())

total_grape = the_vineyard_sq_mt * grape_for_sq_mt
wine = 0.40 * total_grape / 2.5
diff = abs(needed_wine_lt - wine)
if wine < needed_wine_lt:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(diff / num_workers)} liters per person.')
