while True:
    doubled_char_word = ''
    word = input()
    if word == 'End':
        break
    elif word == 'SoftUni':
        continue
    for char in word:
        doubled_char_word += char * 2
    print(doubled_char_word)
