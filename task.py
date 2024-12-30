import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for letters
letters_for_password = []
for letter in range(1, nr_letters + 1):
    letters_for_password += random.choice(letters)

#for numbers
numbers_for_password = []
for number in range(1, nr_numbers + 1):
    numbers_for_password += random.choice(numbers)

# for symbols
symbols_for_password = []
for symbol in range(1, nr_symbols + 1):
    symbols_for_password += random.choice(symbols)

password_combined_list = []
password_combined_list = letters_for_password + numbers_for_password + symbols_for_password

#easy version
string_Combined_password = ""
for char in password_combined_list:
    string_Combined_password += char
print(f"Your easy choice of password can be '{string_Combined_password}'")

#hard version
H_Combined_password = ""
random.shuffle(password_combined_list)
for char in password_combined_list:
    H_Combined_password += char
print(f"You hard choice of password can be '{H_Combined_password}'")



