import random

# Ask the user for the desired password length
def get_length():
    length = input("Enter the desired password length: ")
    try:
        length = int(length)
        return length
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_length()

# Ask the user to choose the character set for the password
def get_includes():
    include = input("Include in password? [N] Numbers only, [A] Numbers and characters: ").upper()
    if include in ["A", "N"]:
        return include
    else:
        print("Invalid choice. Please enter 'N' or 'A'.")
        return get_includes()

# Confirm the user's password preferences
def user_conditions():
    length = get_length()
    include = get_includes()
    confirm = input(
        f"\nThe requested password will have {length} characters and include "
        f"{'NUMBERS AND CHARACTERS' if include == 'A' else 'NUMBERS ONLY'}.\n"
        f"Press ENTER to confirm or type anything to cancel: "
    )
    if confirm == "":
        print("Confirmed.")
        return length, include
    else:
        print("Canceled.")
        return user_conditions()

# Generate a password based on user-defined settings
def password_generator():
    generated_password = []
    pass_length, pass_include = user_conditions()
    numbers = [str(number) for number in range(10)]
    ascii_letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    characters =list("!@#$%^&*()_-+={}[]:;\"\'<>.?/")
    full_characters = characters + numbers + ascii_letters

    for _ in range(pass_length):
        if pass_include == "N":
            num = str(random.randint(0, 9))
            generated_password.append(num)
        else:
            generated_password.append(random.choice(full_characters))

    return "".join(generated_password)


# if __name__ == "__main__":
#     password_generator()



