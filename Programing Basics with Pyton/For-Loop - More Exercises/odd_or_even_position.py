import sys

n = int(input())

oddmax_num = -sys.maxsize
oddmin_num = sys.maxsize
odd_sum = 0
evenmax_num = -sys.maxsize
evenmin_num = sys.maxsize
even_sum = 0

for i in range(1, n + 1):
    current_num = float(input())

    if i % 2 == 0:
        even_sum += current_num
        if current_num < evenmin_num:
            evenmin_num = current_num
        if current_num > evenmax_num:
            evenmax_num = current_num
    else:
        odd_sum += current_num
        if current_num < oddmin_num:
            oddmin_num = current_num
        if current_num > oddmax_num:
            oddmax_num = current_num

if even_sum == 0 and odd_sum == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")
elif even_sum == 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={oddmin_num:.2f},")
    print(f"OddMax={oddmax_num:.2f},")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")
elif odd_sum == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={evenmin_num:.2f},")
    print(f"EvenMax={evenmax_num:.2f}")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={oddmin_num:.2f},")
    print(f"OddMax={oddmax_num:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={evenmin_num:.2f},")
    print(f"EvenMax={evenmax_num:.2f}")