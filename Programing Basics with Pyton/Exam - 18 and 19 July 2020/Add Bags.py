price_over_baggage = float(input())
kg_of_baggage = float(input())
days_to_fly = int(input())
num_of_baggage = int(input())
price_for_baggage = 0
if kg_of_baggage < 10:
    price_for_baggage = price_over_baggage * 0.20
elif kg_of_baggage > 20:
    price_for_baggage = price_over_baggage
else:
    price_for_baggage = price_over_baggage / 2

if days_to_fly > 30:
    price_for_baggage *= 1.10
elif days_to_fly < 7:
    price_for_baggage *= 1.40
else:
    price_for_baggage *= 1.15
total_price = price_for_baggage * num_of_baggage
print(f" The total price of bags is: {total_price:.2f} lv. ")
