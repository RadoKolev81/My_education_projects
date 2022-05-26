number_of_paint_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
number_of_eggs = 0
max_eggs = ''
for i in range(number_of_paint_eggs):
    collor_of_egg = input()

    if collor_of_egg == 'red':
        red += 1
    elif collor_of_egg == 'orange':
        orange += 1
    elif collor_of_egg == 'blue':
        blue += 1
    elif collor_of_egg == 'green':
        green += 1

if red > orange and red > blue and red > green:
    max_eggs = 'red'
    number_of_eggs = red
elif orange > red and orange > blue and orange > green:
    max_eggs = 'orange'
    number_of_eggs = orange
elif blue > red and blue > orange and blue > green:
    max_eggs = 'blue'
    number_of_eggs = blue
elif green > red and green > orange and green > blue:
    max_eggs = 'green'
    number_of_eggs = green

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {number_of_eggs} -> {max_eggs}")