import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_arr = []

input_one = int(input("Enter how many letters you would like in your password: "))
input_two = int(input("Enter how many numbers you would like in your password: "))
input_three = int(input("Enter how many symbols you would like in your password: "))

for num1 in range (1, input_one + 1):
    rand_letters = random.choice(letters)
    pass_arr += rand_letters
for num2 in range (1, input_two + 1):
    rand_numbers = random.choice(numbers)
    pass_arr += rand_numbers
for num3 in range (1, input_three + 1):
    rand_symbols = random.choice(symbols)
    pass_arr += rand_symbols

password = ""
random.shuffle(pass_arr)
for char in pass_arr:
    password += char

print(f"Your password is {password}")