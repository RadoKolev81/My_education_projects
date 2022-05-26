number_of_groups = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
total_people = 0
for i in range(number_of_groups):
    member_of_group = int(input())
    total_people += member_of_group
    if member_of_group <= 5:
        g1 += member_of_group
    elif 5 < member_of_group <= 12:
        g2 += member_of_group
    elif 12 < member_of_group <= 25:
        g3 += member_of_group
    elif 25 < member_of_group <= 40:
        g4 += member_of_group
    else:
        g5 += member_of_group

print(f"{(g1 / total_people * 100):.2f}%")
print(f"{(g2 / total_people * 100):.2f}%")
print(f"{(g3 / total_people * 100):.2f}%")
print(f"{(g4 / total_people * 100):.2f}%")
print(f"{(g5 / total_people * 100):.2f}%")