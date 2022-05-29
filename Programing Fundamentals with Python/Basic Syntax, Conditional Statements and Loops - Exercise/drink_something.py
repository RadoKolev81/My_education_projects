age_of_persons = int(input())
whats_drink = ''

if age_of_persons <= 14:
    whats_drink = 'toddy'
elif age_of_persons <= 18:
    whats_drink = 'coke'
elif age_of_persons <= 21:
    whats_drink = 'beer'
else:
    whats_drink = 'whisky'

print(f'drink {whats_drink}')