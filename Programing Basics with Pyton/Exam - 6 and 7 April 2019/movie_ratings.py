import sys

number_of_movies = int(input())
high_rating = 0
low_rating = sys.maxsize
average_rating = 0
highest_rate_movie = ''
lowest_rate_movie = ''
for movie in range(number_of_movies):
    name_of_movie = input()
    movie_rating = float(input())

    if high_rating < movie_rating:
        high_rating = movie_rating
        highest_rate_movie = name_of_movie
    elif low_rating > movie_rating:
        low_rating = movie_rating
        lowest_rate_movie = name_of_movie
    average_rating += movie_rating

print(f"{highest_rate_movie} is with highest rating: {high_rating :.1f}")
print(f"{lowest_rate_movie} is with lowest rating: {low_rating :.1f}")
print(f"Average rating: {(average_rating / number_of_movies):.1f}")
