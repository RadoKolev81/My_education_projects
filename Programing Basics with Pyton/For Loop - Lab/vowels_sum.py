text = input()
sum_of_ch = 0

for ch in text:
    if ch == 'a':
        sum_of_ch += 1
    elif ch == 'e':
        sum_of_ch += 2
    elif ch == 'i':
        sum_of_ch += 3
    elif ch == 'o':
        sum_of_ch += 4
    elif ch == 'u':
        sum_of_ch += 5

print(sum_of_ch)