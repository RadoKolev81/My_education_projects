budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
price_for_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_for_day = 45000
    elif season == "Summer":
        price_for_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_for_day = 17000
    elif season == "Summer":
        price_for_day = 12500
elif destination == "London":
    if season == "Winter":
        price_for_day = 24000
    elif season == "Summer":
        price_for_day = 20250

total_price = number_of_days * price_for_day
if destination == "Dubai":
    total_price *= 0.70
elif destination == "Sofia":
    total_price *= 1.25
diff = abs(total_price - budget)
if budget < total_price:
    print(f"The director needs {diff:.2f} leva more!")
else:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")