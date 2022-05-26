group_of_climbers = int(input())
climbing_musala = 0
climbing_montblanc = 0
climbing_kilimanjaro = 0
climbing_k2 = 0
climbing_everest = 0
total_climbers = 0

for i in range(group_of_climbers):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers
    if number_of_climbers <= 5:
        climbing_musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        climbing_montblanc += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        climbing_kilimanjaro += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        climbing_k2 += number_of_climbers
    elif number_of_climbers > 40:
        climbing_everest += number_of_climbers

print(f"{(climbing_musala / total_climbers * 100):.2f}%")
print(f"{(climbing_montblanc / total_climbers * 100):.2f}%")
print(f"{(climbing_kilimanjaro / total_climbers * 100):.2f}%")
print(f"{(climbing_k2 / total_climbers * 100):.2f}%")
print(f"{(climbing_everest / total_climbers * 100):.2f}%")