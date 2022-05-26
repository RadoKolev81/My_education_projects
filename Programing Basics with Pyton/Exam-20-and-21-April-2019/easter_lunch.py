number_of_cakes = int(input())
number_of_eggs = int(input())
kg_cookies = int(input())

price_for_cakes = number_of_cakes * 3.20
price_for_eggs = number_of_eggs * 4.35
price_for_cookies = kg_cookies * 5.40
price_for_eggs_paint = number_of_eggs * 12 * 0.15
total_costs = price_for_eggs_paint + price_for_cookies + price_for_eggs + price_for_cakes
print(f"{total_costs:.2f}")
