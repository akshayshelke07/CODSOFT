import string
import secrets

def get_user_preferences():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length (min 8): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            length = 8
    except ValueError:
        print("Invalid input. Using default length to 12.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

    return length, use_upper, use_lower, use_digits, use_symbols

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    ambiguous = {'l', 'I', '1', 'O', '0'}

    char_pool = ''
    if use_upper:
        char_pool += ''.join(c for c in string.ascii_uppercase if c not in ambiguous)
    if use_lower:
        char_pool += ''.join(c for c in string.ascii_lowercase if c not in ambiguous)
    if use_digits:
        char_pool += ''.join(c for c in string.digits if c not in ambiguous)
    if use_symbols:
        char_pool += '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    if not char_pool:
        print("No character sets selected. Defaulting to lowercase + digits.")
        char_pool = ''.join(c for c in string.ascii_lowercase + string.digits if c not in ambiguous)
        use_lower = True
        use_digits = True

    password = []
    if use_upper:
        password.append(secrets.choice([c for c in string.ascii_uppercase if c not in ambiguous]))
    if use_lower:
        password.append(secrets.choice([c for c in string.ascii_lowercase if c not in ambiguous]))
    if use_digits:
        password.append(secrets.choice([c for c in string.digits if c not in ambiguous]))
    if use_symbols:
        password.append(secrets.choice('!@#$%^&*()-_=+[]{}|;:,.<>?/'))

    while len(password) < length:
        password.append(secrets.choice(char_pool))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    length, upper, lower, digits, symbols = get_user_preferences()
    pwd = generate_password(length, upper, lower, digits, symbols)
    print(f"Generated Password: {pwd}")

if __name__ == "__main__":
    main()
