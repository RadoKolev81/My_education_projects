import sys

number_of_movie = int(input())

low_rating = sys.maxsize
low_name = ''
max_rating = 0
max_name = ''
sum_of_ratings = 0
for i in range(number_of_movie):
    name_of_movie = input()
    rating = float(input())
    sum_of_ratings += rating
    if rating > max_rating:
        max_rating = rating
        max_name = name_of_movie
    if rating < low_rating:
        low_rating = rating
        low_name = name_of_movie

average_rating = sum_of_ratings / number_of_movie
print(f"{max_name} is with highest rating: {max_rating:.1f}")
print(f"{low_name} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")