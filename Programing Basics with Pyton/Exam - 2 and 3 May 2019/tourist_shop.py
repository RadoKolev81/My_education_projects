budget = float(input())

counter = 0
sum_of_products = 0
while True:
    name_of_product = input()
    if name_of_product == "Stop":
        print(f"You bought {counter} products for {sum_of_products:.2f} leva.")
        break
    price_of_product = float(input())
    counter += 1
    if counter % 3 == 0:
        price_of_product /= 2
    sum_of_products += price_of_product
    budget -= price_of_product
    if budget < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break
