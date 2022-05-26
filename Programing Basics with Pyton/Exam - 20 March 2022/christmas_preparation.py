number_of_paper = int(input())
number_of_fabric = int(input())
number_of_glue = float(input())
percent_discount = int(input())

price_for_paper = number_of_paper * 5.80
price_for_fabric = number_of_fabric * 7.20
price_for_glue = number_of_glue * 1.20
total_price = price_for_paper + price_for_fabric + price_for_glue
price_with_discount = total_price - (total_price * percent_discount / 100)

print(f"{price_with_discount:.3f}")