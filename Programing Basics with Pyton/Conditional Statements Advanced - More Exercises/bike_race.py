num_of_juniors = int(input())
num_of_seniors = int(input())
type_of_trace = input()
tax_for_juniors = 0
tax_for_seniors = 0

if type_of_trace == "trail":
    tax_for_juniors = 5.50
    tax_for_seniors = 7
elif type_of_trace == "cross-country":
    tax_for_juniors = 8
    tax_for_seniors = 9.50
    if num_of_juniors + num_of_seniors >= 50:
        tax_for_juniors *= 0.75
        tax_for_seniors *= 0.75
elif type_of_trace == "downhill":
    tax_for_juniors = 12.25
    tax_for_seniors = 13.75
elif type_of_trace == "road":
    tax_for_juniors = 20
    tax_for_seniors = 21.50

total_sum = num_of_juniors * tax_for_juniors + num_of_seniors * tax_for_seniors
costs = total_sum * 0.95
print(f"{costs:.2f}")
