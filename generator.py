import random
import string

def generate_password(length, use_upper=True, use_numbers=True, use_symbols=True):
    characters = list(string.ascii_lowercase)
    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, upper, numbers, symbols)
        print(f"🔐 Generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")
