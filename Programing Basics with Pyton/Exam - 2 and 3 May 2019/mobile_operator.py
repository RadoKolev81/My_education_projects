years_of_contract = input()
type_of_contract = input()
with_internet = input()
numb_of_months = int(input())
tax_for_month = 0

if years_of_contract == "one":
    if type_of_contract == "Small":
        tax_for_month += 9.98
    elif type_of_contract == "Middle":
        tax_for_month += 18.99
    elif type_of_contract == "Large":
        tax_for_month += 25.98
    elif type_of_contract == "ExtraLarge":
        tax_for_month += 35.99
elif years_of_contract == "two":
    if type_of_contract == "Small":
        tax_for_month += 8.58
    elif type_of_contract == "Middle":
        tax_for_month += 17.09
    elif type_of_contract == "Large":
        tax_for_month += 23.59
    elif type_of_contract == "ExtraLarge":
        tax_for_month += 31.79

if with_internet == "yes" and years_of_contract == "one":
    if tax_for_month <= 10:
        tax_for_month += 5.50
    elif tax_for_month <= 30:
        tax_for_month += 4.35
    elif tax_for_month > 30:
        tax_for_month += 3.85
elif with_internet == "yes" and years_of_contract == "two":
    if tax_for_month <= 10:
        tax_for_month += 5.50
    elif tax_for_month <= 30:
        tax_for_month += 4.35
    elif tax_for_month > 30:
        tax_for_month += 3.85
if years_of_contract == "two":
    tax_for_month *= 0.9625
total_sum = numb_of_months * tax_for_month
print(f"{total_sum:.2f} lv.")
