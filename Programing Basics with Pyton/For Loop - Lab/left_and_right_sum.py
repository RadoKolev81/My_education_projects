n = int(input())
left_sum = 0
right_sum = 0

for iterate in range(2 * n):
    current_numb = int(input())

    if iterate < n:
        left_sum += current_numb
    else:
        right_sum += current_numb

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
