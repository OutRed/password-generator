import random

password_length = 5

lowercase = "abcdefghijklmnopqrstuvwxyz"

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

symbol = "!@#$%^&*();:.>,</?"

password = ""

for index in range(password_length):
    password = password + random.choice(lowercase) + random.choice(uppercase) + random.choice(symbol)

print("Your new secure password is: {}".format(password))
