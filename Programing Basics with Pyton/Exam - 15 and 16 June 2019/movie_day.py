time_for_shot = int(input())
number_of_scenes = int(input())
time_for_scenes = int(input())
field_preparation = time_for_shot * 0.15
time_for_all_scenes = number_of_scenes * time_for_scenes
needed_time = time_for_all_scenes + field_preparation
diff = abs(time_for_shot - needed_time)

if needed_time < time_for_shot:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")