budget = float(input())
numb_of_series = int(input())

for i in range(numb_of_series):
    name_of_series = input()
    price_for_series = float(input())

    if name_of_series == "Thrones":
        budget -= price_for_series * 0.50
    elif name_of_series == "Lucifer":
        budget -= price_for_series * 0.60
    elif name_of_series == "Protector":
        budget -= price_for_series * 0.70
    elif name_of_series == "TotalDrama":
        budget -= price_for_series * 0.80
    elif name_of_series == "Area":
        budget -= price_for_series * 0.90
    else:
        budget -= price_for_series

if budget < 0:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget:.2f} lv.")
