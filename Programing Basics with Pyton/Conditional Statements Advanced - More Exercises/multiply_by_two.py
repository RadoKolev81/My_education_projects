n = float(input())

while n >= 0:
    result = n * 2
    n = float(input())
    print(f'Result: {result:.2f}')
if not n >= 0:
    print('Negative number!')