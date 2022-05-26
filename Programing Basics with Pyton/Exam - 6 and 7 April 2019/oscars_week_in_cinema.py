name_of_movie = input()
type_of_hall = input()
number_of_tickets = int(input())
price_for_ticket = 0
if type_of_hall == "normal":
    if name_of_movie == "A Star Is Born":
        price_for_ticket = 7.50
    elif name_of_movie == "Bohemian Rhapsody":
        price_for_ticket = 7.35
    elif name_of_movie == "Green Book":
        price_for_ticket = 8.15
    elif name_of_movie == "The Favourite":
        price_for_ticket = 8.75
elif type_of_hall == "luxury":
    if name_of_movie == "A Star Is Born":
        price_for_ticket = 10.50
    elif name_of_movie == "Bohemian Rhapsody":
        price_for_ticket = 9.45
    elif name_of_movie == "Green Book":
        price_for_ticket = 10.25
    elif name_of_movie == "The Favourite":
        price_for_ticket = 11.55
elif type_of_hall == "ultra luxury":
    if name_of_movie == "A Star Is Born":
        price_for_ticket = 13.50
    elif name_of_movie == "Bohemian Rhapsody":
        price_for_ticket = 12.75
    elif name_of_movie == "Green Book":
        price_for_ticket = 13.25
    elif name_of_movie == "The Favourite":
        price_for_ticket = 13.95
total_income = price_for_ticket * number_of_tickets
print(f"{name_of_movie} -> {total_income:.2f} lv.")
