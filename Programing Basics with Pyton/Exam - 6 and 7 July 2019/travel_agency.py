city = input()
type_of_packet = input()
vip_discount = input()
days_of_stay = int(input())
price_for_day = 0

if days_of_stay > 7:
    days_of_stay -= 1
if city == "Bansko" or city == "Borovets":
    if type_of_packet == "withEquipment":
        price_for_day = 100
        if vip_discount == "yes":
            price_for_day *= 0.90
    elif type_of_packet == "noEquipment":
        price_for_day = 80
        if vip_discount == "yes":
            price_for_day *= 0.95
elif city == "Varna" or city == "Burgas":
    if type_of_packet == "withBreakfast":
        price_for_day = 130
        if vip_discount == "yes":
            price_for_day *= 0.88
    elif type_of_packet == "noBreakfast":
        price_for_day = 100
        if vip_discount == "yes":
            price_for_day *= 0.93

if city != "Bansko" and city != "Borovets" and city != "Varna" and city != "Burgas":
    print("Invalid input!")
elif type_of_packet != "noEquipment" and type_of_packet != "withEquipment" and type_of_packet != "noBreakfast" and \
        type_of_packet != "withBreakfast":
    print("Invalid input!")
elif days_of_stay < 1:
    print("Days must be positive number!")
else:
    total_price = days_of_stay * price_for_day
    print(f"The price is {total_price:.2f}lv! Have a nice time!")