from math import ceil

number_of_people = int(input())
entrance_tax = float(input())
price_for_shezlong = float(input())
price_for_umbrella = float(input())
needed_shezlongs = ceil(number_of_people * 0.75)
needed_umbrellas = ceil(number_of_people * 0.50)
total_price = (number_of_people * entrance_tax) + \
              (needed_shezlongs * price_for_shezlong) + (needed_umbrellas * price_for_umbrella)
print(f"{total_price:.2f} lv.")