number_of_student = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
total_grade = 0

for i in range(number_of_student):
    grade = float(input())
    if grade >= 5.00:
        g1 += 1
        total_grade += grade
    elif grade >= 4:
        g2 += 1
        total_grade += grade
    elif grade >= 3:
        g3 += 1
        total_grade += grade
    elif grade < 3:
        g4 += 1
        total_grade += grade

print(f"Top students: {(g1 / number_of_student * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(g2 / number_of_student * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(g3 / number_of_student * 100):.2f}%")
print(f"Fail: {(g4 / number_of_student * 100):.2f}%")
print(f"Average: {(total_grade / number_of_student):.2f}")