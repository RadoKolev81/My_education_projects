name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_tickets = float(input())
percent_for_cinema = int(input())

profit_for_day = number_of_days * price_per_tickets
total_profit = profit_for_day * number_of_tickets
total_profit -= total_profit * (percent_for_cinema / 100)

print(f"The profit from the movie {name_of_movie} is {total_profit:.2f} lv.")