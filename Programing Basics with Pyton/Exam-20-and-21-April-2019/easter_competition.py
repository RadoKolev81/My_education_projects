number_of_cake = int(input())
max_points = 0
total_points = 0
number_one = ''
condition = False
for i in range(number_of_cake):
    baker_name = input()
    while True:
        points = input()
        if points == 'Stop':
            break
        points = int(points)
        total_points += points
        if total_points > max_points:
            max_points = total_points
            number_one = baker_name
            condition = True

    print(f"{baker_name} has {total_points} points.")
    total_points = 0

if condition:
    print(f"{number_one} is the new number 1!")

print(f"{number_one} won competition with {max_points} points!")