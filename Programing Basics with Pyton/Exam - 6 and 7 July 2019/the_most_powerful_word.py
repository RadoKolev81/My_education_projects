from math import floor

max_summ = 0
power_word = ''
while True:
    word = input()
    if word == "End of words":
        break
    current_sum = 0
    for char in range(len(word)):
        current_sum += ord(word[char])
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or \
            word[0] == 'u' or word[0] == 'y' or word[0] == 'A' or word[0] == 'E' or \
            word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        current_sum *= len(word)
    else:
        current_sum = floor(current_sum / len(word))
    if max_summ <= current_sum:
        max_summ = current_sum
        power_word = word

print(f"The most powerful word is {power_word} - {max_summ}")

