country = input()
device = input()
grade_of_difficulty = 0
grade_of_performance = 0

if device == "ribbon":
    if country == "Russia":
        grade_of_difficulty = 9.100
        grade_of_performance = 9.400
    elif country == "Bulgaria":
        grade_of_difficulty = 9.600
        grade_of_performance = 9.400
    elif country == "Italy":
        grade_of_difficulty = 9.200
        grade_of_performance = 9.500
elif device == "hoop":
    if country == "Russia":
        grade_of_difficulty = 9.300
        grade_of_performance = 9.800
    elif country == "Bulgaria":
        grade_of_difficulty = 9.550
        grade_of_performance = 9.750
    elif country == "Italy":
        grade_of_difficulty = 9.450
        grade_of_performance = 9.350
elif device == "rope":
    if country == "Russia":
        grade_of_difficulty = 9.600
        grade_of_performance = 9.000
    elif country == "Bulgaria":
        grade_of_difficulty = 9.500
        grade_of_performance = 9.400
    elif country == "Italy":
        grade_of_difficulty = 9.700
        grade_of_performance = 9.150
total_score = grade_of_performance + grade_of_difficulty
estimated_to_max_score = 20 - total_score
percent_of_all_score = (estimated_to_max_score / 20) * 100
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{percent_of_all_score:.2f}%")
