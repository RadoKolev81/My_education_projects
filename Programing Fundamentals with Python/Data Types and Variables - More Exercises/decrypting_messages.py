key = int(input())
num_of_itteract = int(input())
secret_messege = ''

for i in range(num_of_itteract):
    letter = input()
    secret_messege += chr(ord(letter) + key)
print(secret_messege)