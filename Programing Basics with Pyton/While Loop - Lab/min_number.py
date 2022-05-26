import sys

min_number = sys.maxsize

while True:
    comand = input()

    if comand == "Stop":
        break

    if min_number > int(comand):
        min_number = int(comand)

print(min_number)