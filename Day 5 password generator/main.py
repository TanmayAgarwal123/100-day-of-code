#path: 100%20day%20of%20code/Day%205%20password%20generator/main.py
import random

def password():
    print("Welcome to the Password Generator!")
    letters = int(input("How many letters would you like in your password?\n"))
    symbols = int(input("How many symbols would you like?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    password = ""
    for i in range(0, letters):
        password += random.choice("abcdefghijklmnopqrstuvwxyz")
    for i in range(0, symbols):
        password += random.choice("!@#$%^&*()_+")
    for i in range(0, numbers):
        password += random.choice("1234567890")
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    print(f"Your password is {password}")
    
if __name__ == "__main__":
    password()
