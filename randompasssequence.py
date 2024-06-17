import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pass_list = []

num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

for num1 in range(1, num_letters + 1):
    rand_letter = random.choice(letters)
    pass_list += rand_letter

for num2 in range(1, num_numbers + 1):
    rand_number = random.choice(numbers)
    pass_list += rand_number

for num3 in range(1, num_symbols + 1):
    rand_symbol = random.choice(symbols)
    pass_list += rand_symbol

# shuffled_pass = ''.join(random.sample(password, len(password)))
# random.shuffle(pass_list)
# password = ''.join(pass_list)

password = ""
random.shuffle(pass_list)
for char in pass_list:
    password += char

print(f"Your password is: {password}")