numb_of_days = int(input())

treated_patients = 0
untreated_patients = 0
numb_of_medics = 7

for days in range(1, numb_of_days + 1):
    numb_of_pacientes = int(input())

    if days % 3 == 0 and untreated_patients > treated_patients:
        numb_of_medics += 1
    if numb_of_pacientes <= numb_of_medics:
        treated_patients += numb_of_pacientes
    else:
        treated_patients += numb_of_medics
        untreated_patients += numb_of_pacientes - numb_of_medics

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
