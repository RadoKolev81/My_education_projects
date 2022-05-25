hours = int(input())
minutes = int(input())
total_time = (hours * 60) + minutes + 15
current_hours = total_time // 60
current_minutes = total_time % 60

if current_hours > 23:
    print(f'0:{current_minutes:02d}')
else:
    print(f'{current_hours}:{current_minutes:02d}')
