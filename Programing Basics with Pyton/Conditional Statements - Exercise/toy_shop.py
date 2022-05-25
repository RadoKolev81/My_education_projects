price_for_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())
total_price = (count_puzzles * 2.60) + (count_dolls * 3) + \
              (count_bears * 4.10) + (count_minions * 8.20) + (count_trucks * 2)
count_of_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

if count_of_toys >= 50:
    total_price *= 0.75

rent = total_price * 0.10
profit = total_price - rent
difference = abs(profit - price_for_trip)
if profit >= price_for_trip:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
