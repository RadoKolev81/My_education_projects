total_money = float(input())
year_to_live = int(input())
age_of_ivan = 18

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        total_money -= 12000
    else:
        total_money -= 12000 + (50 * age_of_ivan)
    age_of_ivan += 1

if total_money < 0:
    print(f"He will need {abs(total_money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {total_money:.2f} dollars left.")
