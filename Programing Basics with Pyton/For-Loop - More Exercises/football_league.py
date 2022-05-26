stadium_capacity = int(input())
number_of_fans = int(input())

a = 0
b = 0
v = 0
g = 0

for f in range(number_of_fans):
    sector = input()

    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

print(f"{a / number_of_fans * 100:.2f}%")
print(f"{b / number_of_fans * 100:.2f}%")
print(f"{v / number_of_fans * 100:.2f}%")
print(f"{g / number_of_fans * 100:.2f}%")
print(f"{number_of_fans / stadium_capacity * 100:.2f}%")