student = input()
average_grade = 0.0
grades = 1
bad_grades = 0
bad_grades_condition = False

while grades <= 12:
    if bad_grades > 1:
        bad_grades_condition = True
        break
    grade = float(input())
    if grade < 4:
        bad_grades += 1
        continue

    average_grade += grade
    grades += 1

if bad_grades_condition:
    print(f'{student} has been excluded at {grades} grade')
else:
    average_grade = average_grade / 12
    print(f'{student} graduated. Average grade: {average_grade:.2f}')