name_of_actor = input()
academy_points = float(input())
numb_of_jury = int(input())

total_points = academy_points
is_nominated = False

for i in range(numb_of_jury):
    name_of_jury = input()
    points_of_jury = float(input())

    total_points += (len(name_of_jury) * points_of_jury / 2)

    if total_points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")