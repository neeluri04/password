import tkinter as tk
import random
import string

def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
