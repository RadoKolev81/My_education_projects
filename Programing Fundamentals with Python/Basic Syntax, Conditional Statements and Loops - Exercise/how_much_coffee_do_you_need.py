number_of_cofee = 0
command = input()
while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        number_of_cofee += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        number_of_cofee += 2
    command = input()

if number_of_cofee > 5:
    print('You need extra sleep')
else:
    print(f'{number_of_cofee}')