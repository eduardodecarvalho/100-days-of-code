import string
import random

letters_lower_case = list(string.ascii_lowercase)
letters_upper_case = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '#', '$', '&']

print("Welcome to the PyPassword Generator!")

while True:
    password_size = int(input("How many characters would you like in your password? (Minimum size is 4)\n"))
    if password_size >= 4:
        break
    print("Password size must be at least 4. Please try again.")

password = [
    random.choice(letters_lower_case),
    random.choice(letters_upper_case),
    random.choice(numbers),
    random.choice(symbols)
]

remaining_size = password_size - 4
all_characters = letters_lower_case + letters_upper_case + numbers + symbols
password.extend(random.choices(all_characters, k=remaining_size))

random.shuffle(password)

generated_password = ''.join(password)
print(f"Your generated password is: {generated_password}")

