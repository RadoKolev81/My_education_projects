budget = float(input())

while True:
    name_of_actor = input()

    if name_of_actor == "ACTION":
        break
    if budget < 0:
        break
    if len(name_of_actor) > 15:
        budget -= budget * 0.20
    else:
        payment = float(input())
        budget -= payment

if budget < 0:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")
