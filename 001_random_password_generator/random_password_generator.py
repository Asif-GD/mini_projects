# credit - 100 Days of Code: The Complete Python Pro Bootcamp
# https://www.udemy.com/course/100-days-of-code/

"""
random password generator using letters, symbols and numbers
pseudocode:
1. ask user inputs for three questions
- how many letters?
- how many numbers?
- how many symbols?
2. choose from them at random and build the password.
3. shuffle
"""
import random
import string

print("Welcome to PyPassword Generator!")

password_list: [list] = []

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_digits = int(input("How many numbers would you like in your password? "))
number_of_punctuations = int(input("How many symbols would you like in your password? "))

for number in range(number_of_letters):
    password_list.append(random.choice(string.ascii_letters))

for number in range(number_of_digits):
    password_list.append(random.choice(string.digits))

for number in range(number_of_punctuations):
    password_list.append(random.choice(string.punctuation))

random.shuffle(password_list)

# convert password list to a password string
password_string: [str] = ''
for char in password_list:
    password_string += char

print(f"Here is your generated password: {password_string}")
