destination = input()
date_of_trip = input()
numb_of_nights = int(input())
price_for_nights = 0

if destination == "France":
    if date_of_trip == "21-23":
        price_for_nights = 30
    elif date_of_trip == "24-27":
        price_for_nights = 35
    elif date_of_trip == "28-31":
        price_for_nights = 40
elif destination == "Italy":
    if date_of_trip == "21-23":
        price_for_nights = 28
    elif date_of_trip == "24-27":
        price_for_nights = 32
    elif date_of_trip == "28-31":
        price_for_nights = 39
elif destination == "Germany":
    if date_of_trip == "21-23":
        price_for_nights = 32
    elif date_of_trip == "24-27":
        price_for_nights = 37
    elif date_of_trip == "28-31":
        price_for_nights = 43

total_costs = numb_of_nights * price_for_nights
print(f"Easter trip to {destination} : {total_costs:.2f} leva.")
