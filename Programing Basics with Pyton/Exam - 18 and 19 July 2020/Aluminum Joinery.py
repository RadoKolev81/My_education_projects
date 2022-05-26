amount_of_joinery = int(input())
type_joinery = str(input())
delivery = str(input())
price = 0

if type_joinery == "90X130":
    if amount_of_joinery < 30:
        price = 110
    elif 30 <= amount_of_joinery < 60:
        price = 110 * 0.95
    else:
        price = 110 * 0.92
elif type_joinery == "100X150":
    if amount_of_joinery < 40:
        price = 140
    elif 40 <= amount_of_joinery < 80:
        price = 140 * 0.94
    else:
        price = 140 * 0.90
elif type_joinery == "130X180":
    if amount_of_joinery < 20:
        price = 190
    elif 20 <= amount_of_joinery < 50:
        price = 190 * 0.93
    else:
        price = 190 * 0.88
elif type_joinery == "200X300":
    if amount_of_joinery <= 25:
        price = 250
    elif 25 <= amount_of_joinery <= 50:
        price = 250 * 0.91
    else:
        price = 250 * 0.86

total_price = amount_of_joinery * price

if delivery == "With delivery":
    total_price += 60
elif delivery == "Without delivery":
    total_price = total_price

if amount_of_joinery > 99:
    total_price *= 0.96

if amount_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")