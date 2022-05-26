voucher_value = float(input())
number_of_tickets = 0
number_of_others = 0
total_sum = 0

while total_sum < voucher_value:
    command = input()
    if command == 'End':
        break

    if len(command) > 8:
        total_sum += (ord(command[0]) + ord(command[1]))
        if total_sum > voucher_value:
            break
        else:
            number_of_tickets += 1
    else:
        total_sum += ord(command[0])
        if total_sum > voucher_value:
            break
        else:
            number_of_others += 1

print(f"{number_of_tickets}")
print(f"{number_of_others}")