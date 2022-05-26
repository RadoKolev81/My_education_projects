from math import floor

record_in_sec = float(input())
distance_in_mt = float(input())
sec_per_mt = float(input())

georgi_time = distance_in_mt * sec_per_mt
total_time = (floor(distance_in_mt / 50)) * 30
final_time = georgi_time + total_time

if final_time < record_in_sec:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    diff = abs(final_time - record_in_sec)
    print(f"No! He was {diff:.2f} seconds slower.")