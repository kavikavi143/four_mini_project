import random
import string

def generate_password(length=10, include_digits=True, include_special_chars=True):
    # Characters to choose from for generating passwords
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine all characters to create the pool for password generation
    characters = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate a random password using the pool of characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length:  ")) #(default is 10):
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length=password_length, include_digits=include_digits, include_special_chars=include_special_chars)
    print(f"Generated Password: {password}")
