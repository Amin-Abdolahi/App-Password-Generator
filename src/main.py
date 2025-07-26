import json
import os
from utils.PasswordGenerator import password_generator

DATA_PATH = "data/passwords.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)

def get_username():
    return input("Enter your username: ").strip()

def get_note():
    return input("Enter a note or URL (optional): ").strip()

def show_passwords(data):
    print("\nHow do you want to search?")
    print("[1] By username")
    print("[2] By note")
    print("[3] Show all")
    choice = input("Choice: ").strip()

    if choice == "1":
        username = input("Enter username: ").strip()
        if username in data:
            print(f"\nUsername: {username}")
            print(f"Password: {data[username]['password']}")
            print(f"Note: {data[username]['note']}")
        else:
            print("No data found for this username.")
    
    elif choice == "2":
        keyword = input("Enter keyword in note or URL: ").strip().lower()
        found = False
        for username, details in data.items():
            if keyword in details['note'].lower():
                print(f"\nUsername: {username}")
                print(f"Password: {details['password']}")
                print(f"Note: {details['note']}")
                found = True
        if not found:
            print("No matching note found.")
    
    elif choice == "3":
        if not data:
            print("No passwords saved yet.")
        else:
            for username, details in data.items():
                print(f"\nUsername: {username}")
                print(f"Password: {details['password']}")
                print(f"Note: {details['note']}")
    else:
        print("Invalid option!")

def password_manager():
    print("Welcome to your password manager!")
    data = load_data()

    order = input("Show [s] or Create [c] a new password? ").lower()

    if order == "c":
        password = password_generator()
        confirm = input(f"\nGenerated Password: {password}\nDo you want to save it? [y/n]: ").lower()
        if confirm == "y":
            username = get_username()
            note = get_note()
            data[username] = {
                "password": password,
                "note": note
            }
            save_data(data)
            print("✅ Password saved successfully.")
        else:
            print("❌ Password not saved.")
    elif order == "s":
        show_passwords(data)
    else:
        print("Invalid input. Please type 's' or 'c'.")

password_manager()
