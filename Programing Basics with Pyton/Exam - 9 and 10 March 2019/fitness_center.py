number_of_people = int(input())
people_fit_back = 0
people_fit_chest = 0
people_fit_legs = 0
people_fit_abs = 0
people_take_protein_shake = 0
people_take_protein_bar = 0

for i in range(number_of_people):
    fit_product = input()

    if fit_product == 'Back':
        people_fit_back += 1
    elif fit_product == 'Chest':
        people_fit_chest += 1
    elif fit_product == 'Legs':
        people_fit_legs += 1
    elif fit_product == 'Abs':
        people_fit_abs += 1
    elif fit_product == 'Protein shake':
        people_take_protein_shake += 1
    elif fit_product == 'Protein bar':
        people_take_protein_bar += 1

people_for_fit = (people_fit_abs + people_fit_chest + people_fit_legs + people_fit_back) / number_of_people * 100
people_for_protein = (people_take_protein_shake + people_take_protein_bar) / number_of_people * 100

print(f"{people_fit_back} - back")
print(f"{people_fit_chest} - chest")
print(f"{people_fit_legs} - legs")
print(f"{people_fit_abs} - abs")
print(f"{people_take_protein_shake} - protein shake")
print(f"{people_take_protein_bar} - protein bar")
print(f"{people_for_fit:.2f}% - work out")
print(f"{people_for_protein:.2f}% - protein")