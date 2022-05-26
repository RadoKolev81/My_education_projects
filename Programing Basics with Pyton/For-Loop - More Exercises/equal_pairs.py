num = int(input())
num_1 = int(input())
num_2 = int(input())
result = num_2 + num_1
diff = 0
valid = True

for i in range(1, num):
    current_num_1 = int(input())
    current_num_2 = int(input())

    current_result = current_num_2 + current_num_1

    if current_result != result:

        valid = False
        diff = abs(result - current_result)
        result = current_result

if valid:
    print(f"Yes, value={result}")
else:
    print(f"No, maxdiff={diff}")