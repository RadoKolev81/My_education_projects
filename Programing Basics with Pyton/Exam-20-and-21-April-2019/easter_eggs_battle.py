p1_eggs = int(input())
p2_eggs = int(input())

while True:
    command = input()

    if command == 'End of battle':
        break

    if command == 'one':
        p2_eggs -= 1
        if p2_eggs < 1:
            print(f"Player two is out of eggs. Player one has {p1_eggs} eggs left.")
            break
    elif command == 'two':
        p1_eggs -= 1
        if p1_eggs < 1:
            print(f"Player one is out of eggs. Player two has {p2_eggs} eggs left.")
            break
if p1_eggs > 0 and p2_eggs > 0:
    print(f"Player one has {p1_eggs} eggs left.")
    print(f"Player two has {p2_eggs} eggs left.")
