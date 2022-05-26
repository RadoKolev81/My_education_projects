counter = 0
most_word = ''

while True:
    word = input()

    if word == 'End of words':
        break

    current_counter = 0
    for ch in word:
        current_counter += ord(ch)

    if word[0].lower() in 'aeoiuy':
        current_counter *= len(word)

    else:
        current_counter = int(current_counter / len(word))

    if current_counter > counter:
        counter = current_counter
        most_word = word

print(f"The most powerful word is {most_word} - {counter}")