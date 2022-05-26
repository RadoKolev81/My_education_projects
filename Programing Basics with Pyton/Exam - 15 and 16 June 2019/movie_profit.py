name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_for_ticket = float(input())
percent_for_theater = int(input())
total_price = number_of_tickets * price_for_ticket * number_of_days
theater_tax = total_price * (percent_for_theater / 100)
total_income = total_price - theater_tax
print(f"The profit from the movie {name_of_movie} is {total_income:.2f} lv.")
