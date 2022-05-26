number_of_tabs = int(input())
salary = int(input())
lost_your_salary = False

for tab in range(number_of_tabs):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= 150
    elif current_tab == "Instagram":
        salary -= 100
    elif current_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        lost_your_salary = True
        break

if lost_your_salary:
    print(f"You have lost your salary.")
else:
    print(salary)
