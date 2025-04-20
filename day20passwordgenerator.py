import random

# Character set for passwords
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def password_generator(length):
    if length < 6:
        print("Error: Password length must be at least 6!")
        return ""
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

name = input("Please enter your name: ")
print(f"Hey {name}, let's generate secure passwords for your Liverpool FC accounts!")

while True:
    while True:
        try:
            length = input("Enter password length (6 or more. Or type 'quit'): ").lower()
            if length == 'quit':
                print(f"Goodbye {name}! Stay secure with your Anfield logins!")
                break
            length = int(length)
            if length < 6:
                print("Invalid. Please enter a number equal to or greater than 6.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    
    # Check for quit before calling password_generator
    if length != 'quit':
        result = password_generator(length)
        if result:  # Only print if password was generated
            print(f"Hey {name}, here is your new Anfield password: {result}")
    else:
        break  # Exit outer loop on quit
