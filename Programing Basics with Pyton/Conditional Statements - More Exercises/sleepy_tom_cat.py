num_day_off = int(input())
num_workdays = 365 - num_day_off
time_for_play = (num_workdays * 63) + (num_day_off * 127)
diff = abs(30000 - time_for_play)
hours = diff // 60
minutes = diff % 60

if 30000 < time_for_play:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
