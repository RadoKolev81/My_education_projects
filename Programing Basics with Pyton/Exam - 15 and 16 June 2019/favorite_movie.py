best_movie = ""
max_points = 0
counter = 0
current_points = 0
while True:
    movie = input()
    if movie == "STOP":
        break
    counter += 1
    if counter == 7:
        break
    points = 0
    for ch in movie:
        if ch.isupper() and ch.isalpha():
            points = ord(ch) - len(movie)
            current_points += points
        elif ch.islower() and ch.isalpha():
            points = ord(ch) - len(movie) * 2
            current_points += points
        else:
            points = ord(ch)
            current_points += points
    if current_points > max_points:
        max_points = current_points
        best_movie = movie
    current_points = 0
if counter == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
