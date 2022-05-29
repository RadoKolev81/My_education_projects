first_string = input()
second_string = input()
mutate_string = first_string

for symbol_index in range(len(first_string)):
    left_part = second_string[0:symbol_index + 1:1]
    right_part = first_string[symbol_index + 1:len(first_string):1]
    current_string = left_part + right_part
    if current_string == mutate_string:
        continue
    print(current_string)
    mutate_string = current_string
