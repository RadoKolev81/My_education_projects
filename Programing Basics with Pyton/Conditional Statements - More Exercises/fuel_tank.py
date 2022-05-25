type_fuel = input()
lt_fuel = int(input())

if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    if lt_fuel < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
    else:
        print(f"You have enough {type_fuel.lower()}.")
else:
    print("Invalid fuel!")
