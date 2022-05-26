number = int(input())

for current_number in range(1111, 9999 + 1):
    number_is_special = True
    current_number_as_string = str(current_number)
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_special = False
            break
    if number_is_special:
        print(current_number, end=' ')

# special_number = int(input())
#
# for first_num in range(1, 10):
#     for second_num in range(1, 10):
#         for third_num in range(1, 10):
#             for forth_num in range(1, 10):
#                 if special_number % first_num == 0 and special_number % second_num == 0 \
#                         and special_number % third_num == 0 and special_number % forth_num == 0:
#                     print(f'{first_num}{second_num}{third_num}{forth_num}', end=' ')
