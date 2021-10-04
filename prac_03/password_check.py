"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def get_password():
    return input("> ")

def judge_len(password):
    a = len(password)
    if (a > MAX_LENGTH) or (a < MIN_LENGTH):
        return False
    else:
        return "*" * len(password)

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    print(judge_len(password))
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.upper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return  False
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return  False

    return True
main()