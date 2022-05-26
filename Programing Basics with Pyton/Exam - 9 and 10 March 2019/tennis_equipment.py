from math import floor, ceil

price_of_tennis_racket = float(input())
numb_of_tennis_racket = int(input())
numb_sneakers = int(input())

price_for_all_racket = price_of_tennis_racket * numb_of_tennis_racket
price_for_sneakers = price_of_tennis_racket / 6
price_for_all_sneakers = price_for_sneakers * numb_sneakers
price_for_extra_equipment = (price_for_all_racket + price_for_all_sneakers) * 0.2
total_price = price_for_extra_equipment + price_for_all_sneakers + price_for_all_racket
price_for_djokovic = total_price / 8
price_for_sponsors = total_price * (7 / 8)

print(f"Price to be paid by Djokovic {floor(price_for_djokovic)}")
print(f"Price to be paid by sponsors {ceil(price_for_sponsors)}")
