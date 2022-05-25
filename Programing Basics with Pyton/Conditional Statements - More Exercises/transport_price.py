kilometers = int(input())
daytime = input()
price = 0

if kilometers < 20:
    price = 0.70
    if daytime == 'day':
        price += 0.79 * kilometers
    elif daytime == 'night':
        price += 0.90 * kilometers
elif kilometers >= 100:
    price = 0.06 * kilometers
else:
    price = 0.09 * kilometers

print(f'{price:.2f}')