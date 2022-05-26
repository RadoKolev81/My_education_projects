name_of_projection = input()
type_of_packet = input()
number_of_tickets = int(input())
price_for_ticket = 0

if name_of_projection == "John Wick":
    if type_of_packet == "Drink":
        price_for_ticket = 12
    elif type_of_packet == "Popcorn":
        price_for_ticket = 15
    elif type_of_packet == "Menu":
        price_for_ticket = 19
elif name_of_projection == "Star Wars":
    if type_of_packet == "Drink":
        price_for_ticket = 18
    elif type_of_packet == "Popcorn":
        price_for_ticket = 25
    elif type_of_packet == "Menu":
        price_for_ticket = 30
    if number_of_tickets >= 4:
        price_for_ticket *= 0.70
elif name_of_projection == "Jumanji":
    if type_of_packet == "Drink":
        price_for_ticket = 9
    elif type_of_packet == "Popcorn":
        price_for_ticket = 11
    elif type_of_packet == "Menu":
        price_for_ticket = 14
    if number_of_tickets == 2:
        price_for_ticket *= 0.85
total_price = number_of_tickets * price_for_ticket
print(f"Your bill is {total_price:.2f} leva.")
