kg_of_food = int(input())
gr_of_foood = kg_of_food * 1000
total_food = 0
command = input()
while command != 'Adopted':
    total_food += int(command)

    command = input()
diff = abs(total_food - gr_of_foood)
if total_food > gr_of_foood:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")