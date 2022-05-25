from math import pi

figure = input()
area_of_figure = 0
if figure == 'square':
    a = float(input())
    area_of_figure = a * a
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area_of_figure = a * b
elif figure == 'circle':
    r = float(input())
    area_of_figure = pi * (r ** 2)
elif figure == 'triangle':
    b = float(input())
    h = float(input())
    area_of_figure = (b * h) / 2
print(f'{area_of_figure:.3f}')
