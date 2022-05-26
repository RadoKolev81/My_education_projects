month = int(input())

electricity = 0
water = 0
internet = 0

for bill in range(month):
    current_bill = float(input())
    electricity += current_bill
    water += 20
    internet += 15

other = (electricity + water + internet) + ((electricity + water + internet) * 0.20)
average = (electricity + water + internet + other) / month
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")
