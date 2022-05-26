n = int(input())

even_sum = 0
odd_sum = 0

for iterate in range(n):
    current_numb = int(input())

    if iterate % 2 == 0:
        even_sum += current_numb
    else:
        odd_sum += current_numb

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")