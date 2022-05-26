starting_eggs = int(input())
total_eggs = starting_eggs
sell_eggs = 0
while True:
    command = input()

    if command == 'Close':
        print("Store is closed!")
        print(f"{sell_eggs} eggs sold.")
        break

    numer_of_eggs = int(input())
    if command == 'Buy':
        if numer_of_eggs > total_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {total_eggs}.")
            break
        total_eggs -= numer_of_eggs
        sell_eggs += numer_of_eggs

    elif command == 'Fill':
        total_eggs += numer_of_eggs
