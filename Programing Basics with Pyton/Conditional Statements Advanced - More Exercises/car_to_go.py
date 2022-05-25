budget = float(input())
season = input()
type_class = ""
type_vehicle = ""
if budget <= 100:
    type_class = "Economy class"
    if season == "Summer":
        budget *= 0.35
        type_vehicle = "Cabrio"
    elif season == "Winter":
        budget *= 0.65
        type_vehicle = "Jeep"
elif 100 < budget <= 500:
    type_class = "Compact class"
    if season == "Summer":
        budget *= 0.45
        type_vehicle = "Cabrio"
    elif season == "Winter":
        budget *= 0.80
        type_vehicle = "Jeep"
elif budget > 500:
    type_class = "Luxury class"
    if season == "Summer":
        budget *= 0.90
        type_vehicle = "Jeep"
    elif season == "Winter":
        budget *= 0.90
        type_vehicle = "Jeep"

print(f"{type_class}")
print(f"{type_vehicle} - {budget:.2f}")