season = input()
type_of_group = input()
number_of_student = int(input())
number_of_stays = int(input())
sports = ""
price_for_stay = 0
if season == "Winter":
    if type_of_group == "boys":
        sports = "Judo"
        price_for_stay = 9.60
    elif type_of_group == "girls":
        sports = "Gymnastics"
        price_for_stay = 9.60
    elif type_of_group == "mixed":
        sports = "Ski"
        price_for_stay = 10
elif season == "Spring":
    if type_of_group == "boys":
        sports = "Tennis"
        price_for_stay = 7.20
    elif type_of_group == "girls":
        sports = "Athletics"
        price_for_stay = 7.20
    elif type_of_group == "mixed":
        sports = "Cycling"
        price_for_stay = 9.50
elif season == "Summer":
    if type_of_group == "boys":
        sports = "Football"
        price_for_stay = 15
    elif type_of_group == "girls":
        sports = "Volleyball"
        price_for_stay = 15
    elif type_of_group == "mixed":
        sports = "Swimming"
        price_for_stay = 20
total_price = number_of_student * number_of_stays * price_for_stay
if 10 <= number_of_student < 20:
    total_price *= 0.95
elif 20 <= number_of_student < 50:
    total_price *= 0.85
elif number_of_student >= 50:
    total_price *= 0.50

print(f"{sports} {total_price:.2f} lv.")