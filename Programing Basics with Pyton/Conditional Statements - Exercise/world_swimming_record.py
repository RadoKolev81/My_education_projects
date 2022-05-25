world_record = float(input())
distance = float(input())
time_per_meter = float(input())
ivan_time = distance * time_per_meter

delay = (distance // 15) * 12.5
total_time = ivan_time + delay
diff = abs(total_time - world_record)
if total_time < world_record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
