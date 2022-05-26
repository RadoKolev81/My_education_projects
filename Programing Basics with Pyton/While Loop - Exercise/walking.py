steps_counter = 0

while steps_counter < 10000:
    current_steps = input()

    if current_steps == "Going home":
        steps_to_home = int(input())
        steps_counter += steps_to_home
        break

    steps_counter += int(current_steps)

diff = abs(steps_counter - 10000)
if steps_counter < 10000:
    print(f"{diff} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
