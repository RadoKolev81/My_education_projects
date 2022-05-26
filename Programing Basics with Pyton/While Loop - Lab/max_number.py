import sys

max_number = -sys.maxsize

while True:
    comand = input()

    if comand == "Stop":
        break

    if max_number < int(comand):
        max_number = int(comand)

print(max_number)