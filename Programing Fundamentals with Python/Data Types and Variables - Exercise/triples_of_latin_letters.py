number_of_symbol = int(input())

for first_simbol in range(number_of_symbol):
    for second_simbol in range(number_of_symbol):
        for third_simbol in range(number_of_symbol):
            print(f'{chr(97 + first_simbol)}{chr(97 + second_simbol)}{chr(97 + third_simbol)}')