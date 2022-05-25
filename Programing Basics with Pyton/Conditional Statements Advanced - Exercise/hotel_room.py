month = input()
count_of_stay = int(input())
price_for_studio = 0
price_for_apartment = 0
if month == "May" or month == "October":
    price_for_studio = 50
    price_for_apartment = 65
    if 7 < count_of_stay <= 14:
        price_for_studio *= 0.95
    elif count_of_stay > 14:
        price_for_studio *= 0.70
        price_for_apartment *= 0.90
elif month == "June" or month == "September":
    price_for_studio = 75.20
    price_for_apartment = 68.70
    if count_of_stay > 14:
        price_for_studio *= 0.80
        price_for_apartment *= 0.90
elif month == "July" or month == "August":
    price_for_studio = 76
    price_for_apartment = 77
    if count_of_stay > 14:
        price_for_apartment *= 0.90

total_price_for_studio = price_for_studio * count_of_stay
total_price_for_apartment = price_for_apartment * count_of_stay
print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")
