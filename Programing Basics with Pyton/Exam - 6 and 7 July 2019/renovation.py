from math import ceil

height_of_wall = int(input())
width_of_wall = int(input())
percent_of_not_painting = int(input())
area = height_of_wall * width_of_wall * 4
area_for_painting = ceil(area - (area * percent_of_not_painting / 100))
painted_area = 0

paint = input()
while paint != 'Tired!':
    painted_area += int(paint)
    if painted_area >= area_for_painting:
        break
    paint = input()

diff = abs(painted_area - area_for_painting)
if paint != 'Tired!':
    if painted_area == area_for_painting:
        print("All walls are painted! Great job, Pesho!")
    else:
        print(f'All walls are painted and you have {diff} l paint left!')
else:
    print(f'{diff} quadratic m left.')