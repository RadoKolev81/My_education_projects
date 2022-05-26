min_walking_per_day = int(input())
numb_of_walking_per_day = int(input())
consume_cal_per_day = int(input())

total_min_walking = min_walking_per_day * numb_of_walking_per_day
total_cal = total_min_walking * 5

if total_cal >= consume_cal_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_cal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_cal}.")
