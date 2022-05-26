width = int(input())
length = int(input())
heigth = int(input())
total_volume = width * length * heigth

while total_volume > 0:
    command = input()

    if command == "Done":
        break

    total_volume -= int(command)

if total_volume > 0:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")