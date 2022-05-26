numb_of_turns = int(input())

total_score = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for numb in range(numb_of_turns):
    current_number = int(input())

    if 0 <= current_number <= 9:
        total_score += current_number * 0.20
        from_0_to_9 += 1
    elif 10 <= current_number <= 19:
        total_score += current_number * 0.30
        from_10_to_19 += 1
    elif 20 <= current_number <= 29:
        total_score += current_number * 0.40
        from_20_to_29 += 1
    elif 30 <= current_number <= 39:
        total_score += 50
        from_30_to_39 += 1
    elif 40 <= current_number <= 50:
        total_score += 100
        from_40_to_50 += 1
    elif current_number < 0 or current_number > 50:
        total_score /= 2
        invalid_numbers += 1

print(f"{total_score:.2f}")
print(f"From 0 to 9: {(from_0_to_9 / numb_of_turns * 100):.2f}%")
print(f"From 10 to 19: {(from_10_to_19 / numb_of_turns * 100):.2f}%")
print(f"From 20 to 29: {(from_20_to_29 / numb_of_turns * 100):.2f}%")
print(f"From 30 to 39: {(from_30_to_39 / numb_of_turns * 100):.2f}%")
print(f"From 40 to 50: {(from_40_to_50 / numb_of_turns * 100):.2f}%")
print(f"Invalid numbers: {(invalid_numbers / numb_of_turns * 100):.2f}%")