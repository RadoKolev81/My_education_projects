rent_for_hall = int(input())
price_for_statuette = rent_for_hall * 0.70
price_for_keturing = price_for_statuette * 0.85
price_for_sound = price_for_keturing / 2
total_price = rent_for_hall + price_for_statuette + price_for_keturing + price_for_sound
print(f"{total_price:.2f}")