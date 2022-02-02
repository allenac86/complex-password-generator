import random

character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*-_.1234567890"
password_length = 16

password = "".join(random.sample(character_set, password_length))

print(password)