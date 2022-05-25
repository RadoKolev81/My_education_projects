from math import floor, ceil

num_magnolias = int(input())
num_zumbuls = int(input())
num_roses = int(input())
num_cactus = int(input())
price_for_gift = float(input())
total_sum = (num_magnolias * 3.25) + (num_zumbuls * 4) + (num_roses * 3.5) + (num_cactus * 8)
tax = 0.05 * total_sum
profit = total_sum - tax
diff = abs(profit - price_for_gift)
if profit < price_for_gift:
    print(f"She will have to borrow {ceil(diff)} leva." )
else:
    print(f"She is left with {floor(diff)} leva.")
