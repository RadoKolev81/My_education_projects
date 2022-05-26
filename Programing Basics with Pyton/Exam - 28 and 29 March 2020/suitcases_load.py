load_capacity = float(input())
counter = 0
no_free_space = False
total_space = 0
while True:
    bagage_volume = input()
    if bagage_volume == 'End':
        break
    bagage_volume = float(bagage_volume)
    total_space += bagage_volume
    if total_space >= load_capacity:
        no_free_space = True
        print("No more space!")
        break
    else:
        counter += 1
        if counter > 2:
            bagage_volume *= 1.10

if not no_free_space:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")
