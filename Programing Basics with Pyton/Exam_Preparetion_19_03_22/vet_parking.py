number_of_days = int(input())
number_of_hours = int(input())
total_cost = 0


for day in range(1, number_of_days +1):
    current_cost = 0

    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_cost += 2.50
            total_cost += 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            current_cost += 1.25
            total_cost += 1.25

        else:
            current_cost += 1
            total_cost += 1

    print(f"Day: {day} - {current_cost:.2f} leva")
print(f"Total: {total_cost:.2f} leva")