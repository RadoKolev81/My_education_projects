n = int(input())
condition = False

for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(0, 9):
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    condition = True
                    break
                if (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    condition = True
                    break
            if condition:
                break
        if condition:
            break
    if condition:
        break
if not condition:
    print("Nothing found")