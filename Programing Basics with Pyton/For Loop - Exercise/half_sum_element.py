import sys

n = int(input())

bigger_num = -sys.maxsize
sum_of_numbers = 0

for i in range(n):
    current_num = int(input())

    if current_num > bigger_num:
        bigger_num = current_num

    sum_of_numbers += current_num

if (sum_of_numbers - bigger_num) == bigger_num:
    print("Yes")
    print(f"Sum = {bigger_num}")
else:
    diff = abs((sum_of_numbers - bigger_num) - bigger_num)
    print("No")
    print(f"Diff = {diff}")