
while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    total_sum = 0
    while budget > total_sum:
        current_sum = float(input())
        total_sum += current_sum
        if total_sum >= budget:
            print(f"Going to {destination}!")
            continue
