from math import floor

name_of_serial = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
time_of_normal_episode = float(input())
time_for_reklams = time_of_normal_episode * 0.20
time_of_normal_episode_with_reklams = time_of_normal_episode + time_for_reklams
extra_time_of_special_episodes = number_of_seasons * 10
total_time = time_of_normal_episode_with_reklams * number_of_seasons * number_of_episodes + \
             extra_time_of_special_episodes
print(f"Total time needed to watch the {name_of_serial} series is {floor(total_time)} minutes.")
