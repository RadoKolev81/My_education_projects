championship_stage = input()
type_of_ticket = input()
number_of_ticket = int(input())
picture_with_trophy = input()
price_for_ticket = 0

if type_of_ticket == "Standard":
    if championship_stage == "Quarter final":
        price_for_ticket = 55.50
    elif championship_stage == "Semi final":
        price_for_ticket = 75.88
    elif championship_stage == "Final":
        price_for_ticket = 110.10
elif type_of_ticket == "Premium":
    if championship_stage == "Quarter final":
        price_for_ticket = 105.20
    elif championship_stage == "Semi final":
        price_for_ticket = 125.22
    elif championship_stage == "Final":
        price_for_ticket = 160.66
elif type_of_ticket == "VIP":
    if championship_stage == "Quarter final":
        price_for_ticket = 118.90
    elif championship_stage == "Semi final":
        price_for_ticket = 300.40
    elif championship_stage == "Final":
        price_for_ticket = 400

total_price = number_of_ticket * price_for_ticket
if total_price > 4000:
    total_price *= 0.75
elif 2500 < total_price <= 4000:
    total_price *= 0.90
    if picture_with_trophy == "Y":
        total_price += number_of_ticket * 40

print(f"{total_price:.2f}")
