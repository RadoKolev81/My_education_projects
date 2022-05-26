import sys

n = int(input())

bigger_numb = -sys.maxsize
smaller_numb = sys.maxsize

for numb in range(n):
    current_num = int(input())

    if current_num > bigger_numb:
        bigger_numb = current_num

    if current_num < smaller_numb:
        smaller_numb = current_num

print(f'Max number: {bigger_numb}')
print(f'Min number: {smaller_numb}')