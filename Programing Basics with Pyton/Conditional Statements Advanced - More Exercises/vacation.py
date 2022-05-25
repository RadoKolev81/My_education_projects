budget = float(input())
season = input()
type_of_seat = ""
destination = ""

if budget <= 1000:
    type_of_seat = "Camp"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.65
    elif season == "Winter":
        destination = "Morocco"
        budget *= 0.45
elif 1000 < budget <= 3000:
    type_of_seat = "Hut"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.80
    elif season == "Winter":
        destination = "Morocco"
        budget *= 0.60
elif budget > 3000:
    type_of_seat = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        budget *= 0.90
    elif season == "Winter":
        destination = "Morocco"
        budget *= 0.90

print(f"{destination} - {type_of_seat} - {budget:.2f}")