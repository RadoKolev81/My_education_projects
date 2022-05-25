hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arriving = int(input())
minute_of_arriving = int(input())

time_of_examine = hour_of_exam * 60 + minute_of_exam
time_of_arriving = hour_of_arriving * 60 + minute_of_arriving
difference = abs(time_of_examine - time_of_arriving)
hours = difference // 60
minutes = difference % 60


if time_of_arriving > time_of_examine:
    print("Late")
    if difference > 59:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")
elif time_of_arriving == time_of_examine:
    print("On time")
elif time_of_arriving < time_of_examine:
    if difference <= 30:
        print("On time")
        print(f"{difference} minutes before the start")
    else:
        print("Early")
        if difference > 59:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{minutes} minutes before the start")
