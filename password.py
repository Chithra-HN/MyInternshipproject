import random
import string

def generate_password(min_length, numbers=True, special_character=True):
    letter  = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letter
    if numbers:
        characters += digits
    if special_character:
        characters += special

    pwd = ""
    meets_criteria = False

    has_number = False
    has_special = False


    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum Length:\n"))
pwd = generate_password(min_length)
print(pwd)