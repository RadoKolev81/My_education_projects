summ = float(input())
summ = int(summ * 100)
coins_counter = 0

while summ > 0:
    if summ >= 200:
        summ -= 200
    elif summ >= 100:
        summ -= 100
    elif summ >= 50:
        summ -= 50
    elif summ >= 20:
        summ -= 20
    elif summ >= 10:
        summ -= 10
    elif summ >= 5:
        summ -= 5
    elif summ >= 2:
        summ -= 2
    elif summ >= 1:
        summ -= 1
    coins_counter += 1

print(coins_counter)