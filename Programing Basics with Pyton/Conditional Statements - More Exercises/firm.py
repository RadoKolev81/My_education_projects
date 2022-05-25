needed_hours = int(input())
days = int(input())
overtime_workers = int(input())

total_days = days * 0.90
total_hours = total_days * 8
hours_overtime = overtime_workers * (2 * days)
final_hours = int(total_hours + hours_overtime)
diff = abs(final_hours - needed_hours)
if final_hours < needed_hours:
    print(f'Not enough time!{diff} hours needed.')
else:
    print(f'Yes!{diff} hours left.')
