width = int(input())
length = int(input())
total_pieces = width * length

while total_pieces > 0:
    current_pieces = input()

    if current_pieces == "STOP":
        break

    total_pieces -= int(current_pieces)

if total_pieces <= 0:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")