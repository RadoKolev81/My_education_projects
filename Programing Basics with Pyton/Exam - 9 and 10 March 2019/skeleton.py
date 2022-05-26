minutes_of_control = int(input())
seconds_of_control = int(input())
length_of_gutter_m = float(input())
sec_to_hundred_m = int(input())

control_in_sec = minutes_of_control * 60 + seconds_of_control
time_delay = length_of_gutter_m / 120
total_time_delay = time_delay * 2.5
time_of_marin = (length_of_gutter_m / 100) * sec_to_hundred_m - total_time_delay
diff = abs(control_in_sec - time_of_marin)

if time_of_marin > control_in_sec:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
else:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_marin:.3f}.")
