number_of_seas = int(input())
number_of_mountains = int(input())
profit = 0

while True:
    command = input()
    if command == 'Stop':
        break
    if command == 'sea':
        if number_of_seas < 1:
            continue
        profit += 680
        number_of_seas -= 1
    elif command == 'mountain':
        if number_of_mountains < 1:
            continue
        profit += 499
        number_of_mountains -= 1
    if number_of_seas == 0 and number_of_mountains == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")