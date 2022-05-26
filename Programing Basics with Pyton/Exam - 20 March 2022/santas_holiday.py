days_of_stay = int(input())
type_of_room = input()
evaluation = input()
nights = days_of_stay - 1
price_for_nights = 0

if type_of_room == "apartment":
    price_for_nights += 25
    if nights < 10:
        price_for_nights *= 0.70
    elif 10 <= nights <= 15:
        price_for_nights *= 0.65
    elif nights > 15:
        price_for_nights *= 0.50
if type_of_room == "president apartment":
    price_for_nights += 35
    if nights < 10:
        price_for_nights *= 0.90
    elif 10 <= nights <= 15:
        price_for_nights *= 0.85
    elif nights > 15:
        price_for_nights *= 0.80
if type_of_room == "room for one person":
    price_for_nights += 18

total_price = nights * price_for_nights
if evaluation == "positive":
    total_price += (total_price * 0.25)
elif evaluation == "negative":
    total_price -= (total_price * 0.10)

print(f"{total_price:.2f}")