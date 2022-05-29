n_characters = int(input())
total_sum = 0

for ch in range(n_characters):
    curren_ch = input()
    total_sum += ord(curren_ch)
print(f'The sum equals: {total_sum}')