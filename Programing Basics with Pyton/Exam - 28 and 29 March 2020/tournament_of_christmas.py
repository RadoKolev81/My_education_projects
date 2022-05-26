days_of_tournament = int(input())
total_money = 0
total_wins = 0
total_losts = 0
for i in range(1, days_of_tournament + 1):
    wins = 0
    losts = 0
    money = 0
    while True:
        command = input()
        if command == 'Finish':
            break
        result = input()
        if result == 'win':
            money += 20
            wins += 1
        elif result == 'lose':
            losts += 1
    if wins > losts:
        money += money * 0.10
        total_wins += 1
        total_money += money
    else:
        total_losts += 1
        total_money += money
if total_wins > total_losts:
    total_money += total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
