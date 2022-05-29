string = input()
capital_letters = []
for i in range(len(string)):
    if string[i].isupper():
        capital_letters.append(i)
    else:
        continue

print(capital_letters)