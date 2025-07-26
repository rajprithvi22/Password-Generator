import random
import string

def generate_password():
    print("🔐 Welcome to the Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return

        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        all_chars = uppercase + lowercase + digits + symbols

        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(symbols),
        ]

        password += random.choices(all_chars, k=length - 4)

        random.shuffle(password)

        final_password = ''.join(password)
        print(f"Generated Password: {final_password}")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")

generate_password()
