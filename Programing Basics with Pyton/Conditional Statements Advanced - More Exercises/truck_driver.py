season = input()
km_per_month = float(input())
price_for_km = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_for_km = 0.75
    elif season == "Summer":
        price_for_km = 0.90
    elif season == "Winter":
        price_for_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_for_km = 0.95
    elif season == "Summer":
        price_for_km = 1.10
    elif season == "Winter":
        price_for_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_for_km = 1.45

income = km_per_month * price_for_km * 4
total_income = income * 0.90
print(f"{total_income:.2f}")