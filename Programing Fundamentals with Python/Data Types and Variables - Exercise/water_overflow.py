number_of_itteract = int(input())
capacity = 255
water_quantity = 0

for i in range(number_of_itteract):
    lt_water = int(input())
    if capacity - lt_water < 0:
        print('Insufficient capacity!')
        continue
    water_quantity += lt_water
    capacity -= lt_water
print(water_quantity)