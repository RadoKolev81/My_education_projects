budget = float(input())
season = input()
destination = ""
type_of_seat = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_seat = "Camp"
        budget = budget - (budget * 0.70)
    elif season == "winter":
        type_of_seat = "Hotel"
        budget = budget - (budget * 0.30)
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_seat = "Camp"
        budget = budget - (budget * 0.60)
    elif season == "winter":
        type_of_seat = "Hotel"
        budget = budget - (budget * 0.20)
elif budget > 1000:
    destination = "Europe"
    type_of_seat = "Hotel"
    budget = budget - (budget * 0.10)
print(f"Somewhere in {destination}")
print(f"{type_of_seat} - {budget:.2f}")
