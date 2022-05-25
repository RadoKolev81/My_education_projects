budget = float(input())
category = input()
num_of_people = int(input())
price_for_ticket = 0

if category == "VIP":
    price_for_ticket = 499.99
elif category == "Normal":
    price_for_ticket = 249.99
if 1 <= num_of_people <= 4:
    budget *= 0.25
elif 5 <= num_of_people <= 9:
    budget *= 0.40
elif 10 <= num_of_people <= 24:
    budget *= 0.50
elif 25 <= num_of_people <= 49:
    budget *= 0.60
elif num_of_people >= 50:
    budget *= 0.75
costs = price_for_ticket * num_of_people
difference = abs(budget - costs)
if budget < costs:
    print(f"Not enough money! You need {difference:.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")