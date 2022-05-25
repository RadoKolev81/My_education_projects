count_of_hrizantems = int(input())
count_of_roses = int(input())
count_of_tulips = int(input())
season = input()
holiday_or_not = input()
price_for_hrizantems = 0
price_for_roses = 0
price_for_tulips = 0

if season == "Spring" or season == "Summer":
    price_for_hrizantems = 2.00
    price_for_roses = 4.10
    price_for_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_for_hrizantems = 3.75
    price_for_roses = 4.50
    price_for_tulips = 4.15

if holiday_or_not == "Y":
    price_for_hrizantems *= 1.15
    price_for_roses *= 1.15
    price_for_tulips *= 1.15
total_price = count_of_hrizantems * price_for_hrizantems + \
              count_of_roses * price_for_roses + count_of_tulips * price_for_tulips
if count_of_tulips > 7 and season == "Spring":
    total_price *= 0.95
elif count_of_roses >= 10 and season == "Winter":
    total_price *= 0.90
if count_of_roses + count_of_hrizantems + count_of_tulips > 20:
    total_price *= 0.80
final_price = total_price + 2
print(f"{final_price:.2f}")
