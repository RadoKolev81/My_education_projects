name_of_actor = input()
academy_points = float(input())
number_of_jury = int(input())
total_points = academy_points
nominated = False

for i in range(number_of_jury):
    name_of_jury = input()
    point_of_jury = float(input())
    total_points += len(name_of_jury) * point_of_jury / 2
    if total_points >= 1250.5:
        nominated = True
        break

if nominated:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")