numb_of_pallet = int(input())

buss = 0
truck = 0
train = 0
total_price = 0

for i in range(numb_of_pallet):
    current_pallet = int(input())

    if current_pallet <= 3:
        buss += current_pallet
        total_price += current_pallet * 200
    elif 4 <= current_pallet <= 11:
        truck += current_pallet
        total_price += current_pallet * 175
    else:
        train += current_pallet
        total_price += current_pallet * 120

total_pallet = buss + truck + train
print(f"{total_price / total_pallet:.2f}")
print(f"{buss / total_pallet * 100:.2f}%")
print(f"{truck / total_pallet * 100:.2f}%")
print(f"{train / total_pallet * 100:.2f}%")