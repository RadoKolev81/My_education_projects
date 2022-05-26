best_name = ''
total_sum = 0
final_sum = 0

while True:
    name = input()
    if name == 'Stop':
        break
    for ch in name:
        current_num = int(input())
        if current_num == ord(ch):
            total_sum += 10
        else:
            total_sum += 2
    if total_sum >= final_sum:
        final_sum = total_sum
        best_name = name
    total_sum = 0

print(f"The winner is {best_name} with {final_sum} points!")
