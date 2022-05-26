numb_of_bad_grades = int(input())
bad_grades = 0
solved_problems = 0
sum_of_grades = 0
last_problem = ""
is_failed = True

while bad_grades < numb_of_bad_grades:
    name_of_problem = input()
    if name_of_problem == "Enough":
        is_failed = False
        break
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
    sum_of_grades += current_grade
    solved_problems += 1
    last_problem = name_of_problem

if is_failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {sum_of_grades / solved_problems:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")

