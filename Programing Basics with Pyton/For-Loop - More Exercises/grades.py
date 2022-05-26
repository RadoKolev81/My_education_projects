numb_of_student = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
average = 0

for i in range(numb_of_student):
    current_grade = float(input())

    if 2 <= current_grade <= 2.99:
        fail += 1
    elif 3 <= current_grade <= 3.99:
        between_3_and_4 += 1
    elif 4 <= current_grade <= 4.99:
        between_4_and_5 += 1
    elif current_grade >= 5:
        top_students += 1
    average += current_grade

print(f"Top students: {(top_students / numb_of_student * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_and_5 / numb_of_student * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_and_4 / numb_of_student * 100):.2f}%")
print(f"Fail: {(fail / numb_of_student * 100):.2f}%")
print(f"Average: {(average / numb_of_student):.2f}")
