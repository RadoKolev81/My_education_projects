from math import ceil

name_of_serial = input()
length_of_serial = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_relax = time_for_break / 4
estimated_time = time_for_break - time_for_lunch - time_for_relax

diff = abs(estimated_time - length_of_serial)
if estimated_time < length_of_serial:
    print(f"You don't have enough time to watch {name_of_serial}, you need {ceil(diff)} more minutes.")
else:
    print(f"You have enough time to watch {name_of_serial} and left with {ceil(diff)} minutes free time.")
