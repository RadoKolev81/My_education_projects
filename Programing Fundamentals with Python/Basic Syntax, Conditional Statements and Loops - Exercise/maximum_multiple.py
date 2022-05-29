divisor = int(input())
boundary = int(input())
n = 0

for current_num in range(boundary, divisor, - 1):
    if current_num % divisor == 0:
        n = current_num
        break
print(n)