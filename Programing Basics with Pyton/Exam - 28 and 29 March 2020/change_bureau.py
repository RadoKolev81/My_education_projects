numb_of_bitcoins = int(input())
numb_of_juans = float(input())
tax = float(input())

bitcoins_to_bgn = numb_of_bitcoins * 1168
juans_to_usd = numb_of_juans * 0.15
juans_to_bgn = juans_to_usd * 1.76
total_bgn = bitcoins_to_bgn + juans_to_bgn
total_euro = total_bgn / 1.95
final_euro = total_euro - (total_euro * tax / 100)

print(f"{final_euro:.2f}")
