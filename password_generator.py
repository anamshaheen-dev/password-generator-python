# Password Generator
# Built by: Anum Shaheen

import random
import string

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters
    guaranteed = []

    if use_digits:
        characters += string.digits
        guaranteed.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        guaranteed.append(random.choice(string.punctuation))

    remaining = [random.choice(characters) for _ in range(length - len(guaranteed))]
    password_list = guaranteed + remaining
    random.shuffle(password_list)

    return "".join(password_list)
def menu():
    print("==============================")
    print("     Password Generator       ")
    print("==============================")

    while True:
        print("\nOptions:")
        print("1. Generate Password")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == '1':
            while True:
                try:
                    length = int(input("Enter password length (6-32): "))
                    if 6 <= length <= 32:
                        break
                    else:
                        print("Please enter a number between 6 and 32!")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            digits = input("Include numbers? (yes/no): ").lower() == 'yes'
            symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

            password = generate_password(length, digits, symbols)
            print(f"\nYour password is: {password}")

        elif choice == '2':
            print("Goodbye! Stay safe online!")
            break

        else:
            print("Invalid choice! Please enter 1 or 2.")

# This runs the app
menu()