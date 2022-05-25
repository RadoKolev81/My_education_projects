days_of_stay = int(input())
type_of_room = input()
grade = input()
price = 0
nights_of_stay = days_of_stay - 1
if type_of_room == "room for one person":
    price = 18.00
elif type_of_room == "apartment":
    price = 25.00
    if nights_of_stay < 10:
        price *= 0.70
    elif 10 <= nights_of_stay <= 15:
        price *= 0.65
    elif nights_of_stay > 15:
        price *= 0.50
elif type_of_room == "president apartment":
    price = 35.00
    if nights_of_stay < 10:
        price *= 0.90
    elif 10 <= nights_of_stay <= 15:
        price *= 0.85
    elif nights_of_stay > 15:
        price *= 0.80
total_price = nights_of_stay * price
if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.90
print(f"{total_price:.2f}")
