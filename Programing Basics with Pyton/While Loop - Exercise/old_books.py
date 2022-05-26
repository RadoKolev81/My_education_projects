searched_book = input()

checked_books = 0
is_found = False

while True:
    current_book = input()

    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    elif current_book == searched_book:
        print(f"You checked {checked_books} books and found it.")
        break
    checked_books += 1