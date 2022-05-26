price_for_party = float(input())
number_of_messeges = int(input())
number_of_roses = int(input())
number_of_keyholder = int(input())
number_of_caricatures = int(input())
number_of_surprice = int(input())

total_sum = (number_of_messeges * 0.60) + (number_of_roses * 7.20) + (number_of_keyholder * 3.60) + \
            (number_of_caricatures * 18.20) + (number_of_surprice * 22)
number_of_artikul = number_of_keyholder + number_of_surprice + number_of_caricatures + \
                    number_of_roses + number_of_messeges

if number_of_artikul > 25:
    total_sum -= (total_sum * 0.35)

profit = total_sum * 0.90
diff = abs(profit - price_for_party)

if profit >= price_for_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")